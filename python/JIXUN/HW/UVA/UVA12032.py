import sys
lines = sys.stdin.read().strip().split('\n')
T = int(lines[0])
index = 0
def solve(k, ladder):
    for i in range(len(ladder) - 1):
        diff = ladder[i + 1] - ladder[i]
        if diff > k: return False
        if diff == k: k -= 1
    return True

for _ in range(1, T + 1):
    index += 1
    n = int(lines[index])
    ladder = [0]
    index += 1
    line = lines[index].split(' ')
    for __ in range(len(line)):
        ladder.append(int(line[__]))
#     # print(ladder)
    low = 0
    high = int(ladder[-1])
    
    while high - low > 1:
        mid = (high + low) // 2
        # print('high:', high)
        # print('low:', low)
        if solve(mid, ladder):
            high = mid
        else: low = mid
    print('Case {}: {}'.format(_, low + 1))




#     diffs = {}
#     for height in range(len(ladder) - 1):
#         diff = ladder[height + 1] - ladder[height]
#         if diff in diffs: diffs[diff] += 1
#         else: diffs[diff] = 1
#     # print(diffs)
#     if diffs[max(diffs)] > 1:
#         k = max(diffs) +  1
#     else: k = max(diffs)
#     print('Case {}: {}'.format(_, k)) 

