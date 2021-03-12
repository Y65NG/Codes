from multiprocessing import Pool
import time
from collections import deque

def test(strr):
    return strr % 2 == 0

if __name__ == '__main__':
    p = Pool(10)
    q = deque()
    for i in range(10):
        q.append(p.apply_async(test, args = (i, )))
    while 1:
        if q.pop():
            p.terminate()
            break
    p.join()