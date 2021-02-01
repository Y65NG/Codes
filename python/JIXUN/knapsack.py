c = int(input())
items = []
while True:
    line = input()
    if line == '': break
    data = list(map(int, line.split(' ')))
    items.append((data[0], data[1]))
n = len(items)

def max_value(c, items):
    memo = [[0] * (c + 1) for _ in range(n + 1)]
    memo[0] = [0] + [-float('inf') for _ in range(c)]
    # print(memo)
    for i in range(1, n + 1):
        for j in range(0, c + 1):
            up = memo[i - 1][j]
            if j - items[i - 1][0] >= 0: left = memo[i - 1][j - items[i - 1][0]] + items[i - 1][1]
            else: left = -float('inf')
            memo[i][j] = max(up, left)
    return memo[n][c]
print(max_value(c, items))
