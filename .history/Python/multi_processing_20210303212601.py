from multiprocessing import Pool
import time

def test(strr):
    i = strr
    time.sleep(1)
    return i

if __name__ == '__main__':
    p = Pool(10)
    for i in range(10):
        result = p.map(test, (i, ))
        print(result)