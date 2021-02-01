def len_of_series(num):
    total = 1
    while num != 1:
        total += 1
        if num % 2 == 0: num = num // 2
        else: num = 3 * num + 1
    return total
# 29

def sqrt(num):
    result = num / 2
    while abs(num - result * result) > 0.000001: result = (result + num / result) / 2
    # if abs(result - int(result)) < 0.00001: return int(result)
    return result
# 1.4142135623746899

def greatest_prime_factor(num):
    while num % 2 == 0: num = num // 2
    for factor in range(3, int(num ** 0.5) + 1, 2):
        while num % factor == 0: 
            num = num // factor
        if num == 1: return factor
    return num
# 394024499311

print(sqrt(100))
