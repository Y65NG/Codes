import sys
lines = open('loan.in', 'r').read().strip().split(' ')
# lines = sys.stdin.read().strip().split(' ')
N, K, M = int(lines[0]), int(lines[1]), int(lines[2])
def check(X):
    return N // X + (K - 1) * M >= N

ans = 0
low = 1
high = N // M
while high - low > 1:
    mid = (low + high) // 2
    if check(mid): low = mid
    else: high = mid
if check(high):
    ans = high
else: ans = low
file = open('loan.out', 'w')
file.write(str(ans))
file.close()
print(ans)