import sys

lines = sys.stdin.read().strip().split('\n')
M, N = [int(x) for x in lines[0].split(' ')]
scopes = []
sequence = [1] * (M + 1)
for i in range(1, N + 1):
    line = [int(x) for x in lines[i].split(' ')]
    scopes.append(line)
for scope in scopes:
    for i in range(scope[0], scope[1] + 1):
        if scope[2] % sequence[i] == 0: sequence[i] *= scope[2] // sequence[i]
        else: sequence[i] *= scope[2]
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
temp = sequence[:]
check = True
for scope in scopes:
    for i in range(scope[0], scope[1] + 1):
        temp[i] //= scope[2]
    for j in range(scope[0], scope[1]):
        # print(gcd(j, j + 1), )
        if gcd(sequence[j], sequence[j + 1]) != 1: 
            print('Impossible')
            print(temp)
            check = False
if check: 
    for i in range(1, len(sequence)): 
        print(sequence[i], end = ' ')