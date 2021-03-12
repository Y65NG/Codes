import sys

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
friends = []
for i in range(1, N + 1):
    friends.append([int(x) for x in lines[i].split(' ')])
print(N, friends)