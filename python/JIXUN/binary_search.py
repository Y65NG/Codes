import random

# 小了返回 false，大了返回 true
def is_valid(guess, secret):
    return guess <= secret

def binary_search(max):
    secret = int(random.random() * 1000)
    print('secret:',secret)
    high = max
    low = 0

    while high - low >  1:
        mid = (high + low) // 2
        if not is_valid(mid, secret):
            high = mid
        else: 
            low = mid
        
    print(low)
binary_search(1000)