import sys

def get_time(p, d, v):
    return abs(p - d) * v

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
friends = []
for i in range(1, N + 1):
    friends.append([int(x) for x in lines[i].split(' ')])
# print(N, friends)

low_t = 0
high_t = 1000000000000
while high_t - low_t > 1:
    