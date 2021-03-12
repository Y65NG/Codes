import sys

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
heights = [int(x) for x in lines[1].split(' ')]
widths = [int(x) for x in lines[2].split(' ')]
print(N, heights, widths)