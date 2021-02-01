import time
def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeFactor(num):
    start = time.time()
    factors = []
    i = 2
    while i <= num:
        if isPrime(i):
            #print(i)
            if num % i == 0:
                factors.append(i)
                num /= i
            else: i += 1
        else: i += 1
    print(factors)
    print(time.time() - start)

while True:
    primeFactor(int(input()))