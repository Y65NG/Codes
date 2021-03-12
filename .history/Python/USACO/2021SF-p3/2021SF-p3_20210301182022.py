import sys

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
grids = []
for i in range(1, N + 1):
    line = [int(x) for x in lines[i].split(' ')]
    grids.append(line)
print(grids)
