from multiprocessing import Pool
import time, random

def fn():
    time.sleep(2)
if __name__ == '__main__':
    p = Pool(10)
    start = time.time()
    for i in range(8):
        p.apply_async(fn)
    p.close()
    p.join()
    end = time.time()
    print(end - start)
    print('1')


