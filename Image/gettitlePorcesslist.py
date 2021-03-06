from multiprocessing import Pool
import os, time, random
import requests

def long_time_task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("task %s run %0.2f second" % (name,0))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args = (i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
