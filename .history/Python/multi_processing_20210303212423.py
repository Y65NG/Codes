from multiprocessing import Pool

def test(strr):
    i = strr
    return i

if __name__ == '__main__':
    p = Pool(10)
    result = p.map(test, ('world', ))
    print(result)