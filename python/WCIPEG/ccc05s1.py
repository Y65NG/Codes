t = int(input())
def change(letter):
    if ord(letter) >= 65 and ord(letter) <= 67: return '2'
    if ord(letter) >= 68 and ord(letter) <= 70: return '3'
    if ord(letter) >= 71 and ord(letter) <= 73: return '4'
    if ord(letter) >= 74 and ord(letter) <= 76: return '5'
    if ord(letter) >= 77 and ord(letter) <= 79: return '6'
    if ord(letter) >= 80 and ord(letter) <= 83: return '7'
    if ord(letter) >= 84 and ord(letter) <= 86: return '8'
    if ord(letter) >= 87 and ord(letter) <= 90: return '9'
    else: return letter

for _ in range(t):
    line = input()
    digit = []
    for i in line:
        if i != '-': digit.append(i)
    for i in range(len(digit)):
        digit[i] = change(digit[i])
    index = 0
    while index < 10:
        if index == 3 or index == 6:
            print('-', end = '')
            print(digit[index], end = '')
        else: print(digit[index], end = '')
        index += 1
    print()

