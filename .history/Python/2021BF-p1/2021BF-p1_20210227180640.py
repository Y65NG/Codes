import sys

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
names = {}
for i in range(1, N + 1):
    line = lines[i].split(' ')
