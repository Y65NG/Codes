from multiprocessing import Pool
import time
from deque import deque

def test(strr):
    return strr % 2 == 0

if __name__ == '__main__':
    p = Pool(10)
    q = queue.queue
    for i in range(10):
        result = p.map(test, (i, ))
        print(result)