import ray
import time
import numpy as np

# DEFINITIONS
MAP_DIM = int(1e3)
SPICE_FIELD_PROB = 0.01
SPICE_FILE_SKEW = 0.7
S3_FILE = 2
OBJ_FILE = 1
NUM_ACTORS = 4


@ray.remote(resources={"head": 0.9}, name="GameState")
class GameState:
    """
    DO NOT MODIFY

    Actor which creates and manages the game state.
    """
    def __init__(self):
        # initialize empty fedaykin and rival actors; this will be set externally by a call to .set_actors()
        self.fedaykin_actors = None
        self.rival_actors = None

        # initialize dictionary containing messages passed between workers
        self.fedaykin_messages = {to_id: {from_id: [] for from_id in range(1, 5)} for to_id in range(1, 5)}
        self.rival_messages = {to_id: {from_id: [] for from_id in range(1, 5)} for to_id in range(1, 5)}

        # create northern and southern spice field maps
        self.n_spice_loc_map, self.n_spice_file_map, self.n_order_map = self._create_map("northern")
        self.s_spice_loc_map, self.s_spice_file_map, self.s_order_map = self._create_map("southern")

        # create (and put) ray objects for both spice fields
        self.n_spice_field_refs = self._create_spice_fields("northern")
        self.s_spice_field_refs = self._create_spice_fields("southern")


    def set_actors(self, fedaykin_actors, rival_actors):
        self.fedaykin_actors = fedaykin_actors
        self.rival_actors = rival_actors

    def get_spice_field_ref(self, hemisphere, i, j):
        spice_field_refs = self.n_spice_field_refs if hemisphere == "northern" else self.s_spice_field_refs
        return spice_field_refs[(i, j)]

    def send_message(self, to_id, from_id, msg, fedaykin_or_rival):
        if fedaykin_or_rival == "fedaykin":
            self.fedaykin_messages[to_id][from_id].append(msg)
        else:
            self.rival_messages[to_id][from_id].append(msg)

    def get_new_messages(self, to_id, from_id, fedaykin_or_rival):
        if fedaykin_or_rival == "fedaykin":
            msgs = self.fedaykin_messages[to_id][from_id]
            self.fedaykin_messages[to_id][from_id] = []
            return msgs
        else:
            msgs = self.rival_messages[to_id][from_id]
            self.rival_messages[to_id][from_id] = []
            return msgs

    def update_spice_field_ref(self, spice_field, i, j, hemisphere):
        spice_field_ref = ray.put(spice_field)
        if hemisphere == "northern":
            self.n_spice_field_refs[(i,j)] = spice_field_ref
        else:
            self.s_spice_field_refs[(i,j)] = spice_field_ref

    def _create_map(self, hemisphere):
        print(f"Creating {hemisphere} spice map")
        
        # create locations of spice fields
        spice_loc_map = np.random.binomial(1, p=SPICE_FIELD_PROB, size=(MAP_DIM, MAP_DIM))

        # decide whether spice field file will be "in S3" or in obj. store
        s3_map = np.random.binomial(1, p=SPICE_FILE_SKEW, size=(MAP_DIM, MAP_DIM))
        obj_map = (s3_map==0).astype(int)
        spice_file_map = spice_loc_map * s3_map * S3_FILE + spice_loc_map * obj_map * OBJ_FILE

        # compute necessary order of destruction
        order_map = {}
        out = np.where(spice_loc_map==1)
        for i, j in zip(out[0], out[1]):
            order_map[(i,j)] = np.random.choice([1,2,3,4], size=np.random.choice([1,2,3,4]), replace=False)

        return spice_loc_map, spice_file_map, order_map

    def _create_spice_fields(self, hemisphere):
        print(f"Creating {hemisphere} spice fields")
        spice_loc_map = self.n_spice_loc_map if hemisphere == "northern" else self.s_spice_loc_map

        spice_field_refs = {}
        out = np.where(spice_loc_map==1)
        for i, j in zip(out[0], out[1]):
            spice_field_object = {"payload": "", "writes": [], "location": [i, j]}
            spice_field_ref = ray.put(spice_field_object)
            spice_field_refs[(i,j)] = spice_field_ref

        return spice_field_refs

    def start_game(self) -> float:
        """
        Starts the game and returns the start time to the driver.
        """
        print("Starting Game")
        start_time = time.time()
        for idx in range(NUM_ACTORS):
            self.rival_actors[idx].start.remote(self.s_spice_loc_map, self.s_spice_file_map, self.s_order_map)
            self.fedaykin_actors[idx].start.remote(self.n_spice_loc_map, self.n_spice_file_map, self.n_order_map)

        return start_time

    def end_game(self) -> bool:
        # stop all the actors
        for idx in range(NUM_ACTORS):
            ray.kill(self.rival_actors[idx])
            ray.kill(self.fedaykin_actors[idx])
        print("Game Over")
        print("Tallying results...")

        def _compute_player_spice_destroyed(hemisphere):
            fedaykin_spice_destroyed = 0
            rival_spice_destroyed = 0

            # compute total spice for each player in the given hemisphere
            spice_loc_map = self.n_spice_loc_map if hemisphere == "northern" else self.s_spice_loc_map
            order_map = self.n_order_map if hemisphere == "northern" else self.s_order_map
            spice_field_refs = self.n_spice_field_refs if hemisphere == "northern" else self.s_spice_field_refs
            out = np.where(spice_loc_map==1)
            for i, j in zip(out[0], out[1]):
                spice_field = ray.get(spice_field_refs[(i,j)])
                i = spice_field["location"][0]
                j = spice_field["location"][1]
                if np.array_equal(spice_field["writes"], order_map[(i,j)]):
                    if spice_field["payload"] == "fedaykin":
                        fedaykin_spice_destroyed += 1
                    elif spice_field["payload"] == "rival":
                        rival_spice_destroyed += 1
                    else:
                        raise Exception("Payload is wackadoodle")
            
            return fedaykin_spice_destroyed, rival_spice_destroyed

        # compute spice destroyed in each hemisphere
        fedaykin_northern_spice_destroyed, rival_northern_spice_destroyed = _compute_player_spice_destroyed("northern")
        fedaykin_southern_spice_destroyed, rival_southern_spice_destroyed = _compute_player_spice_destroyed("southern")

        # compute total spice destroyed
        fedaykin_total_spice_destroyed = fedaykin_northern_spice_destroyed + fedaykin_southern_spice_destroyed
        rival_total_spice_destroyed = rival_northern_spice_destroyed + rival_southern_spice_destroyed

        # return total_spice_value destroyed by each actor
        return fedaykin_total_spice_destroyed, rival_total_spice_destroyed
