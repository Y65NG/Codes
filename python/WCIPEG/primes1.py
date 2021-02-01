N = int(input())
n = 0
num = 2
def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True
while n < N:
    if is_prime(num): 
        print(num)
        n += 1
    num += 1
    
        