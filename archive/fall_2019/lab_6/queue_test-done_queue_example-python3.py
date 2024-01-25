import multiprocessing
import queue
import json
import sys
import time

#VERBOSE = False
VERBOSE = True


# Useful for debugging concurrency issues.
def log(msg):
    if not VERBOSE:
        return

    print(multiprocessing.current_process().name, msg, file=sys.stderr)


# Each worker reads the json file, computes a sum and a count for the target
# field, then stores both in the output queue.
def task(proc_id, in_q, out_q, done_q):
    age_sum = 0
    age_cnt = 0

    while (True):
        try:
            # Just to reduce busy waiting on the queue; works just as well with async.
            item = in_q.get(block=True, timeout=0.05)
        except Queue.Empty:
            # Keep trying! Can only stop if i get a stop msg.
            continue

        if item == 'stop':
            log('read signal to stop, stopping!')
            break

        with open(item) as json_file:
            for line in json_file:
                data = json.loads(line)
                age_sum = age_sum + data["version"]
                age_cnt = age_cnt + 1

    out_q.put((age_sum, age_cnt, item))
    done_q.put('done!')


def main_task(cnt):
    nprocs = int(cnt)

    q = multiprocessing.Queue()
    out_q = multiprocessing.Queue()
    done_q = multiprocessing.Queue()

    # Enqueue filenames to be processed in parallel.
    n_files = 100
    for i in range(n_files):
        f = "data/mybinder%03d.json" % (i)
        q.put(f)

    # Signal to producers that there's no more coming.
    for i in range(nprocs):
        q.put('stop')

    procs = []
    for i in range(nprocs):
        p_name = 'proc-%d' % i
        p = multiprocessing.Process(
            target=task, name=p_name, args=(i, q, out_q, done_q))
        p.start()
        procs.append(p)

    # Make sure the main process does not start consuming before all producers are done.
    for i in range(nprocs):
        item = done_q.get()
        log('dequeued done msg %s' % item)

    log('we can start consumer stage now...')

    # Main task takes partial results and computes the final average.
    sum = 0.0
    cnt = 0

    for p in range(nprocs):
        (p_sum, p_count, item) = out_q.get()
        sum = sum + p_sum
        cnt = cnt + p_count

    print('sum = %s' % sum)
    print('cnt = %s' % cnt)
    print('average = %.2f' % (sum / cnt))


# python3 queue_test.py <n_cores>
if __name__ == "__main__":
    main_task(sys.argv[1])
