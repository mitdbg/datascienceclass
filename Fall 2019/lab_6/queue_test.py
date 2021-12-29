import multiprocessing
import Queue
import json
import sys

#VERBOSE = False
VERBOSE = True


# Useful for debugging concurrency issues.
def log(msg):
    if not VERBOSE:
        return
    print >> sys.stderr, multiprocessing.current_process().name, msg


# Each worker reads the json file, computes a sum and a count for the target
# field, then stores both in the output queue.
def task(in_q, out_q):
    age_sum = 0
    age_cnt = 0

    try:
        while (True):
            f = in_q.get(block=False)
            with open(f) as json_file:
                for line in json_file:
                    data = json.loads(line)
                    age_sum = age_sum + data["version"]
                    age_cnt = age_cnt + 1
    except Queue.Empty:
        pass  #print "Done processing"

    out_q.put((age_sum, age_cnt))


def main_task(cnt):
    nprocs = int(cnt)

    q = multiprocessing.Queue()
    out_q = multiprocessing.Queue()

    # Enqueue filenames to be processed in parallel.
    for i in range(100):
        f = "data/mybinder%03d.json" % (i)
        q.put(f)

    procs = []
    for i in range(nprocs):
        p = multiprocessing.Process(target=task, args=(q, out_q))
        p.start()
        procs.append(p)

    # Main task takes partial results and computes the final average.
    sum = 0.0
    cnt = 0

    for p in procs:
        (p_sum, p_count) = out_q.get()
        sum = sum + p_sum
        cnt = cnt + p_count

    print "average = %.2f" % (sum / cnt)


# python3 queue_test.py <n_cores>
if __name__ == "__main__":
    main_task(sys.argv[1])
