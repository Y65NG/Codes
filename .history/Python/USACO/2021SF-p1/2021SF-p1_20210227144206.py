import sys

lines = sys.stdin.read().strip().split('\n')
N, K = [int(x) for x in lines[0].split(' ')]
cows = [int(x) for x in lines[1:]]
cows.sort()
print(cows)
    