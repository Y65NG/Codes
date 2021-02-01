T = int(input())
for _ in range(T):
    line = input()
    num = 0
    while True:
        try:
            index = line.index('<3')
            line = line[:index] + '__' + line[index + 2:]
            num += 1
        except ValueError:
            break
    for __ in range(num + 1): print('<3', end = ' ')
    print()
        
