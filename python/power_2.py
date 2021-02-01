import time

def isPrime(num):
    for a in range(2, num - 1):
        if num % a == 0:
            return False
    return True

def power(line):
    start = time.time()
    nums = line.split('**')
    
    a = int(nums[0])
    b = int(nums[1])
    result = a
    times = 1
    i = 2
    tempB = b
    while isPrime(tempB) == False:
        times *= i
        tempB /= i
        if i == b:
            break
    
    for j in range(1, times):
        result *= a
    
    for j in range(1, tempB):
        result *= a
    return [result,time.time() - start]

while True:
    print(power(input())[1])