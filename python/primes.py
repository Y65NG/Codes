
#* Prime Testing
def is_prime(num):
    if num % 2 == 0: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0: return False
    return True 
# print(is_prime(49))

#* Prime Generation
def sieve(num):
    nums = [False, False]
    for i in range(2, num + 1): nums.append(True)
    for divisor in range(2, int(num ** 0.5) + 1):
        #* 如果 divisor 所在的 index 判定为质数
        if nums[divisor]:
            for index in range(divisor ** 2, num + 1, divisor):
                nums[index] = False
    result = []
    for i in range(len(nums)): 
        if nums[i]: result.append(i)
    return result
print(sieve(100))

# def scope_sieve(low, high):
#     nums = {}
#     for i in range(low, high + 1): nums[i] = True
#     for divisor in range(low, int(high ** 0.5) + 1):
#         if nums[divisor]:
#             for 

#* Prime Factoring
def prime_factor(num):
    factors = []
    divisor = 2
    while divisor < num:
        while num % divisor == 0:
            num /= divisor
            if num % divisor != 0: factors.append(divisor)
        divisor += 1
    return factors
# prime_factor(25)

#* GCD
def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a % b)
# print(gcd(27,45))

#* LCM
def lcm(a, b):
    return a * b // gcd(a, b)
# print(lcm(27, 45))



