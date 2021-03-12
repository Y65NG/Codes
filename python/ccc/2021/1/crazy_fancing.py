import sys

def cal_area(a, b, h):
    return (a + b) * h / 2

lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
heights = [int(x) for x in lines[1].split(' ')]
widths = [int(x) for x in lines[2].split(' ')]
# print(N, heights, widths)
result = 0
for i in range(len(widths)):
    result += cal_area(heights[i], heights[i + 1], widths[i])
if result % 1 == 0: print(int(result))
else: print(result)
