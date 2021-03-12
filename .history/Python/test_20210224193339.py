arr = []
tree = [] # 树状数组，index 从 1 开始
tree_len = 100

def lowbit(x):
    return x & (-x)
print(lowbit(34))

def add(pos, x):
    for i in range(pos, 101, lowbit(i)): tree[i] += val

def sum(p1, p2):
    result = 0
    for i in range(p1, p2 + 1, lowbit(i)): result += tree[i]

# 逆序对
n = int(input())
arr = [int(x) for x in input().split(' ')]
sorted_arr = sorted(arr)
discrete = 
