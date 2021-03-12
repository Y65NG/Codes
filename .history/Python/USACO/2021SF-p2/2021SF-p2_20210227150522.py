import sys

lines = sys.stdin.read().strip().split('\n')
N, K = [int(x) for x in lines[0].split(' ')]
cows = [int(x) for x in lines[1:]]
cows.sort(reverse = True)
# print(cows)
initial = 0
if cows[0] % 12 == 0:
    initial = cows[0]
else: initial = 12 * (cows[0] // 12 + 1)
# print(initial)

groups = {}
diffs = []
for i in range(len(cows)):
    num = cows[i] // 12
    if num not in groups: 
        groups[num] = 1
        if i != 0:
            diffs.append(cows[i - 1] // 12 - num - 1)
    else: groups[num] += 1
diffs.append(cows[-1] // 12)
print(diffs)
# for num in groups.keys():



# pos = max(groups)
# # print(pos)
# time = 0
# while pos > 0:
