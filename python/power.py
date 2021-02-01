import time
def power(line):
    start = time.time()
    nums = line.split('**')
    a = int(nums[0])
    b = int(nums[1])
    result = a
    for i in range(1, b):
        result *= a
    
    return [result,time.time() - start]

while True:
    print(power(input())[1])