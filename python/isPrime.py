def isPrime(num):
    for a in range(2, num - 1):
        if num % a == 0:
            return False
    return True