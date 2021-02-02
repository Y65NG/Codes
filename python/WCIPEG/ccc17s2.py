import sys

lines = sys.stdin.read().strip().split('\n')
N, tides = int(lines[0]), [int(x) for x in lines[1].split(' ')]
tides.sort()
if N % 2 == 0:
    lows, highs = tides[:N // 2], tides[N // 2:]
else: lows, highs = tides[:N // 2 + 1], tides[N // 2 + 1:]
# print(lows, highs)
lows.sort(reverse = True)
result = []
for i in range(len(highs)):
    result.append(lows[i])
    result.append(highs[i])
if N % 2 != 0: result.append(lows[-1])
# print(result)
for i in result:
    print(i, end = ' ')