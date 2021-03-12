n = int(input())
arr = [int(x) for x in input().split(' ')]
num = 1
while n > 2 ** num:
    num += 1
base_len = 2 **num
tree = [0] * base_len # 第 0 位空着
tree += arr + [0] * (base_len - n)


def i_to_n(index, base_len): return index + base_len

def n_to_i(node, base_len): return node - base_len

def change(pos, num, tree): # pos: the index of changed number in arr
    tree[pos] = num
    if pos % 2 == 0:
        if pos == 1: return
        else: change(pos // 2, num + tree[pos + 1], tree)
    else:
        if pos == 1: return
        else: change((pos - 1) // 2, num + tree[pos - 1], tree)

def total(i1, i2):
    n1, n2 = i_to_n(i1), i_to_n(i2)
    if n1

for i in range(n): change(i_to_n(i, base_len), arr[i], tree)
print(tree)
    



