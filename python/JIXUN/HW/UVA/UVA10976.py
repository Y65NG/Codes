import sys
line = sys.stdin.read().strip().split("\n")
for i in range(len(line)):
    k = int(line[i])
    count = 0
    result = ''
    for y in range(k + 1, 2 * k + 1):
        x = (k * y) // (y - k)
        if k == (x * y) // (x + y):
            count += 1
            result += '\n1/{} = 1/{} + 1/{}'.format(k, x, y)
    result = str(count) + result
    print(result)
