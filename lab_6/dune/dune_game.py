import argparse
import ray
import time

import numpy as np
import scipy as sp

from dune_helpers import *
from dune_rivals import *

# DEFINITIONS
SLEEP_SECONDS_PER_TRAVEL_COORD = 1e-5
SLEEP_SECONDS_READ_FROM_S3     = 0.100
SLEEP_SECONDS_NOT_ON_SPICE     = 1.000


class BaseActor:
    """
    DO NOT MODIFY

    Base class with common functionality shared across all Fedaykin and Rival Actors.
    """
    def __init__(self, payload: str):
        self.payload = payload
        self.i = np.random.randint(0, MAP_DIM - 1)
        self.j = np.random.randint(0, MAP_DIM - 1)
        self.gamestate = ray.get_actor("GameState")
        self.spice_loc_map = None
        self.spice_file_map = None
        self.order_map = None

    def _set_fields(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict) -> None:
        """
        This is technically not necessary but it will save a lot of people issues with a race condition.
        """
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

    def _destroy_spice_field(self) -> bool:
        """
        DO NOT MODIFY

        (Contributes to) destroy(ing) the spice field at location: (self.i, self.j)

        Recall that order_map[(i, j)] returns the order in which your Fedaykin must
        call _destroy_spice_field() in order for the field to be fully destroyed.
        (There is no partial credit for partial destruction).

        The function will return False if the actor fails to destroy the spice field
        because either:

          A. (self.i, self.j) is not a valid spice field location, or
          B. at least one Fedaykin preceding this one in the order_map has not yet
             called _destroy_spice_field() at this location

        The function returns True if the call to destroy the spice field is successful.
        """
        # if this isn't a spice field, incur a delay and return False
        if not self.spice_loc_map[(self.i, self.j)]:
            print(f"Fedaykin{self.id} tried to destroy spice at {(self.i, self.j)}, but this is not a Spice location.")
            print(f"Fedaykin{self.id} sleeping for {SLEEP_SECONDS_NOT_ON_SPICE} seconds")
            time.sleep(SLEEP_SECONDS_NOT_ON_SPICE)
            return False

        # if file is "on S3" simulate extra delay for the network request
        if self.spice_file_map[(self.i, self.j)] == S3_FILE:
            print(f"Fedaykin{self.id} fetching spice field object from S3 for {(self.i, self.j)}")
            time.sleep(SLEEP_SECONDS_READ_FROM_S3)
        else:
            print(f"Fedaykin{self.id} fetching spice field object from OBJECT STORE for {(self.i, self.j)}")

        # get spice field object
        spice_field_ref = ray.get(self.gamestate.get_spice_field_ref.remote("northern", self.i, self.j))
        spice_field = ray.get(spice_field_ref)

        # check if spice field object can be written to
        write_order = self.order_map[(self.i, self.j)]
        try:
            write_idx = np.where(write_order == self.id)[0][0]
        except:
            print(f"Fedaykin{self.id} tried to destroy spice at {(self.i, self.j)} but is not a valid destroyer ({list(write_order)})")
            return False

        if np.array_equal(spice_field["writes"], write_order[:write_idx]):
            spice_field["writes"].append(self.id)
            if np.array_equal(spice_field["writes"], write_order):
                spice_field["payload"] = self.payload
                print(f"Fedaykin{self.id} DESTROYED SPICE FIELD AT ({(self.i, self.j)})")
            else:
                print(f"Fedaykin{self.id} partially destroyed spice field at ({(self.i, self.j)})")
            self.gamestate.update_spice_field_ref.remote(spice_field, self.i, self.j, "northern")
            return True

        else:
            print(f"Fedaykin{self.id} tried to destroy spice at {(self.i, self.j)} but current vs. destruction is: ({spice_field['writes']}) vs. ({list(write_order)})")
            return False


    def _ride_sandworm(self, new_i: int, new_j: int) -> None:
        """
        DO NOT MODIFY

        Moves your Fedaykin to the coordinates (new_i, new_j) and sleeps for the
        appropriate travel duration.
        """
        assert 0 <= new_i and new_i < MAP_DIM, f"New coord. i: {new_i} is off the map"
        assert 0 <= new_j and new_j < MAP_DIM, f"New coord. i: {new_j} is off the map"

        # calculate manhattan distance of movement
        delta_i = abs(new_i - self.i)
        delta_j = abs(new_j - self.j)
        total_dist = delta_i + delta_j

        # sleep for travel duration
        time.sleep(total_dist * SLEEP_SECONDS_PER_TRAVEL_COORD)

        # update coordinates
        self.i = new_i
        self.j = new_j


    def _send_message(self, to_id: int, msg: dict):
        """
        DO NOT MODIFY

        Send a message to another Fedayking via the gamestate. Messages will be placed in
        a list which can be retrieved via a call to self._get_new_messages()
        """
        self.gamestate.send_message.remote(to_id, self.id, msg, "fedaykin")


    def _get_new_messages(self, from_id: int) -> list:
        """
        DO NOT MODIFY

        Returns the messages accumulated for this worker (self.id) which were sent by
        worker from_id since the last time this method was called.
        """
        return ray.get(self.gamestate.get_new_messages.remote(self.id, from_id, "fedaykin"))


@ray.remote(num_cpus=0.8, name="Fedaykin1", resources={"worker1": 1e-4})
class Fedaykin1(BaseActor):
    """
    Fedaykin warrior/actor running on Worker 1 on one of its two CPUs.
    """
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 1


    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict) -> None:
        """
        This is the entrypoint for your first actor's code. Your 4 actors will run in parallel
        distributed across 4 CPUs (each actor runs on 1 CPU, there are 2 CPUs per machine,
        thus 2 actors per node (sometimes also called "worker")).

        The inputs to this function are as follows:

        spice_loc_map: is a 2D numpy array of shape (MAP_DIM, MAP_DIM).
        - if spice_loc_map[i,j] == 1, then there is a spice field at that location

        spice_file_map: is a 2D numpy array of shape (MAP_DIM, MAP_DIM).
        - if spice_file_map[i,j] == 2, then the data file for that spice field is on S3
          (i.e. it will take longer to fetch when calling _destroy_spice_field())
        - if spice_file_map[i,j] == 1, then the data file for that spice field is in Ray's object store
          (i.e. it is in memory on this machine or another one in the cluster and will take less time
           to fetch -- relative to S3 -- when calling _destroy_spice_field())

        order_map: is a dictionary mapping (int, int) tuples to 1D numpy arrays of length 1, 2, 3, or 4
        - for example order_map[(i,j)] might look like one of:
            - array([2])
            - array([3,1,4])
            - array([4,3,1,2])
        - the array specifies (left-to-right) the order in which Fedaykin actors must call _destroy_spice_field()
          for it to be destroyed, for example:
            - if order_map[(i,j)] == array([3,1,4]), then in order to destroy the spice field at location (i,j)
              - first, Fedaykin3 must move to (i, j) and execute _destroy_spice_field()
              - second, Fedaykin1 must move to (i, j) and execute _destroy_spice_field()
              - finally, Fedaykin4 must move to (i, j) and execute _destroy_spice_field()
        """
        # I will set these state variables for you
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

        # TODO: YOUR CODE GOES HERE
        pass


@ray.remote(num_cpus=0.8, name="Fedaykin2", resources={"worker1": 1e-4})
class Fedaykin2(BaseActor):
    """
    Fedaykin warrior/actor running on Worker 1 on one of its two CPUs.
    """
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 2


    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        """
        See comment for start() in Fedaykin1.
        """
        # I will set these state variables for you
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

        # TODO: YOUR CODE GOES HERE
        pass


@ray.remote(num_cpus=0.8, name="Fedaykin3", resources={"worker2": 1e-4})
class Fedaykin3(BaseActor):
    """
    Fedaykin warrior running on Worker 2 on one of its two CPUs.
    """
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 3


    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        """
        See comment for start() in Fedaykin1.
        """
        # I will set these state variables for you
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

        # TODO: YOUR CODE GOES HERE
        pass


@ray.remote(num_cpus=0.8, name="Fedaykin4", resources={"worker2": 1e-4})
class Fedaykin4(BaseActor):
    """
    Fedaykin warrior running on Worker 2 on one of its two CPUs.
    """
    def __init__(self, payload: str):
        super().__init__(payload)
        self.id = 4


    def start(self, spice_loc_map: np.ndarray, spice_file_map: np.ndarray, order_map: dict):
        """
        See comment for start() in Fedaykin1.
        """
        # I will set these state variables for you
        self.spice_loc_map = spice_loc_map
        self.spice_file_map = spice_file_map
        self.order_map = order_map

        # TODO: YOUR CODE GOES HERE
        pass


if __name__ == "__main__":
    """
    DO NOT MODIFY
    """
    # parse arguments
    parser = argparse.ArgumentParser(description='Run an iteration of the Dune Game')
    parser.add_argument('--rival', type=str, help='The rival algorithm')
    args = parser.parse_args()

    # The user has to indicate the rival
    if args.rival is None:
        print("Please provide a rival")
        exit(1)

    elif args.rival not in ["noop", "silly-goose", "glossu-rabban", "feyd-rautha"]:
        print(f"You specified rival: {args.rival}, but --rival must be one of ['noop', 'glossu-rabban', 'feyd-rautha', 'sardaukar']")

    # connect to ray cluster
    ray.init()

    # print Ray job id in all caps
    print(f"JOB ID IS: {ray.runtime_context.get_runtime_context().get_job_id()}")
    print(f"WAITING FOR CLUSTER TO BE AVAILABLE")

    # create game state
    gs = GameState.remote()

    # create fedaykin warriors
    fedaykin_actors = [
        Fedaykin1.remote("fedaykin"),
        Fedaykin2.remote("fedaykin"),
        Fedaykin3.remote("fedaykin"),
        Fedaykin4.remote("fedaykin"),
    ]

    # NOTE: your code interpreter might complain that it doesn't recognize
    #       the rival classes, but they will be installed at runtime by Ray 
    # create rival warriors
    if args.rival == "noop":
        rival_actors = [
            Noop12.remote("rival"),
            Noop12.remote("rival"),
            Noop34.remote("rival"),
            Noop34.remote("rival"),
        ]
    elif args.rival == "silly-goose":
        rival_actors = [
            SillyGoose1.remote("rival"),
            SillyGoose2.remote("rival"),
            SillyGoose3.remote("rival"),
            SillyGoose4.remote("rival"),
        ]
    elif args.rival == "glossu-rabban":
        rival_actors = [
            GlossuRabban1.remote("rival"),
            GlossuRabban2.remote("rival"),
            GlossuRabban3.remote("rival"),
            GlossuRabban4.remote("rival"),
        ]
    elif args.rival == "feyd-rautha":
        rival_actors = [
            FeydRautha1.remote("rival"),
            FeydRautha2.remote("rival"),
            FeydRautha3.remote("rival"),
            FeydRautha4.remote("rival"),
        ]

    # set actors in gamestate
    gs.set_actors.remote(fedaykin_actors, rival_actors)

    # start game
    start_time_ref = gs.start_game.remote()
    start_time = ray.get(start_time_ref)

    # let the game run for 100 seconds
    while time.time() - start_time < 60.0:
        time.sleep(1.0)

    # end the game and return total spice destroyed by each player
    total_spice_values_ref = gs.end_game.remote()
    fedaykin_total_spice_destroyed, rival_total_spice_destroyed = ray.get(total_spice_values_ref)

    # determine the winner and print the outcome
    print(f"FEDAYKIN TOTAL SPICE DESTROYED: {fedaykin_total_spice_destroyed}")
    print(f"RIVAL    TOTAL SPICE DESTROYED: {rival_total_spice_destroyed}")
    print(f"-------------------------------------")
    if fedaykin_total_spice_destroyed > rival_total_spice_destroyed:
        print(f"THE WINNER IS: FEDAYKIN")
    elif fedaykin_total_spice_destroyed < rival_total_spice_destroyed:
        print(f"THE WINNER IS: RIVAL")
    else:
        print(f"THE WINNER IS: IT'S A DRAW")
