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
        sequence[i] *= scope[2]
for i in range(1, len(sequence)): print(sequence[i], end = ' ')