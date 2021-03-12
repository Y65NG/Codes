from multiprocessing import Pool
import time, random

def fn():
    time.sleep(random.randint(0, 2))
if __name__ == '__main__':
    p = Pool(10)
    for i in range(1):
        p.apply_async(fn)
    p.close()
    p.join()
    print('1')


