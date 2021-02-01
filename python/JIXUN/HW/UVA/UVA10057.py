import sys
lines = sys.stdin.read().strip().split('\n')
start = 0
while True:
    n = int(lines[start])
    formula = []
    num_A = 0
    count = 0
    for _ in range(n):
        x = int(lines[start + 1 + _])
        formula.append(x)
    formula.sort()
    if len(formula) % 2 != 0:
        num_A = 1
        median = formula[len(formula) // 2]
    else:
        num_A = 1 + formula[len(formula) // 2] - formula[len(formula) // 2 - 1]
        median = formula[len(formula) // 2 - 1]
    for i in formula:
        if i >= median and i <= formula[len(formula) // 2]: count += 1
    print(median, count, num_A)
    start += n + 1
    if start == len(lines): break