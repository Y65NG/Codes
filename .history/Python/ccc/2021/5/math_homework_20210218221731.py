import sys

lines = sys.stdin.read().strip().split('\n')
M, N = [int(x) for x in lines[0].split(' ')]
scopes = []
sequence = [1] * M
for i in range(1, N + 1):
    