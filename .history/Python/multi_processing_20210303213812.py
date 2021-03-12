from multiprocessing import Pool
import time
from collections import deque

def test(strr):
    return strr % 2 == 0

if __name__ == '__main__':
    p = Pool(10)
    q = deque()
    for i in range(10):
        result = p.map(test, (i, ))
        print(result)