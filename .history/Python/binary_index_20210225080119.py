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
n = int(input())
arr = [0] + [int(x) for x in input().split(' ')]
sorted_arr = sorted(arr)
temp = {sorted_arr[i]:i for i in range(n)}
discrete = [0] * n

for i in range(n):
    discrete[i] = temp[arr[i]]

result = 0
for i in range(1, n + 1):
    result += i - sum(arr[i]) - 1
    add(arr[i], 1)
print(result)
