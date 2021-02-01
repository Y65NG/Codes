import time
def primeFactor(num):
    start = time.time()
    factors = []
    factor = 2
    a = num
    while factor < a:
        # print(factor)
        if num % factor == 0:
            factors.append(factor)
            num /= factor
        else:
            factor += 1
    print(factors)
    print(time.time() - start)
while True:
    primeFactor(int(input()))