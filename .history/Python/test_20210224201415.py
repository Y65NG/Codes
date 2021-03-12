arr = []
tree = [0] * 100 # 树状数组，index 从 1 开始
tree_len = 100

def lowbit(x):
    return x & (-x)
# print(lowbit(34))

def add(pos, x):
    i = pos
    while i < 100:
        tree[i] += val
        i += lowbit(i)
    # for i in range(pos, 101, lowbit(i)): tree[i] += val

def sum(p1, p2):
    result = 0
    for i in range(p1, p2 + 1, lowbit(i)): result += tree[i]

# 逆序对
n = int(input())
arr = [int(x) for x in input().split(' ')]
sorted_arr = sorted(arr)
temp = {sorted_arr[i]:i for i in range(n)}
discrete = [0] * n
for i in range(n):
    discrete[i] = temp[arr[i]]

add(n + 1, 0)
for i in range(n, 0, -1):
    add(i, sum(i + 1, n + 1))
print(tree)
