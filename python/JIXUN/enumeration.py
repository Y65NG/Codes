N = int(input())
def length(num):
    result = 0
    while num % 10 != num: 
        num = num // 10
        result += 1
    return result
def not_duplicate(num):
    digits = set()
    length = 0
    while num % 10 != num:
        digits.add(num % 10)
        num = num // 10
        length += 1
    return len(digits) == length

def no_duplicated_digit(a, b):
    digita = set()
    digitb = set()
    while a % 10 != a:
        digita.add(a % 10)
        a = a // 10
    while b % 10 != b:
        digitb.add(b % 10)
        b //= 10
    for i in digita:
        if i in digitb: return False
    return True
    
def has_zero(num):
    while num % 10 != num:
        if num % 10 == 0: return True
        num //= 10
    return False
        


count = 0
for abcde in range(12345, 98765):
    if abcde % N == 0 and not_duplicate(abcde) and not_duplicate(abcde // N) and no_duplicated_digit(abcde, abcde // N):
        judge = False
        if length(abcde // N) == 4 and not has_zero(abcde):
            judge = True
        if judge: 
            count += 1 
            judge = False

print(count)
