import sys

def get_time(p, d, v):
    return abs(p - d) * v

def valid(pos):


def valid_t(t):
    low = 0
    high = 1000000000
    while high - low > 1:
        mid = (low + high) // 2
        if valid(mid): return True
        else: low = mid
    return high

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
friends = []
for i in range(1, N + 1):
    friends.append([int(x) for x in lines[i].split(' ')])
# print(N, friends)

low_t = 0
high_t = 1000000000000
while high_t - low_t > 1:
    mid_t = (low_t + high_t) // 2
    if valid(mid_t): high_t = mid_t
    else: low_t = mid_t