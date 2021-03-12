tree = [0] * 100 # 树状数组，index 从 1 开始

def lowbit(x):
    return x & (-x)
# print(lowbit(34))

def add(pos, x):
    i = pos
    while i < 100:
        tree[i] += x
        i += lowbit(i)
    # for i in range(pos, 101, lowbit(i)): tree[i] += val

def sum(pos):
    result = 0
    i = pos
    while i >= 1:
        result += tree[i]
        i -= lowbit(i)
    return result
    # for i in range(p1, p2 + 1, lowbit(i)): result += tree[i]

# 逆序对
lines = open('haircut.in').read().strip().split('\n')
n = int(lines[0])
hairs = [0] + [int(x) for x in lines[1].split(' ')]
# sorted_hairs = sorted(hairs)
# temp = {sorted_hairs[i]:i for i in range(n)}
# discrete = [0] * n
# for i in range(n):
#     discrete[i] = temp[hairs[i]]

for _ in range(n):
    temp = hair[]
    result = 0
    for i in range(1, n + 1):
        result += i - sum(hairs[i]) - 1
        add(hairs[i], 1)
    print(result)
