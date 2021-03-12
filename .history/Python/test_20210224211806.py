n = int(input())
arr = [int(x) for x in input().split(' ')]
num = 1
while n > 2 ** num:
    num += 1
base_len = 2 **num
tree = [0] * base_len # 第 0 位空着
tree += arr + [0] * (base_len - n)


def i_to_n(index, n):
    return index + n + 1
def change(pos, num, tree): # pos: the index of changed number in arr
    if pos % 2 != 0:
        if pos == 1: return
        else: change(pos // 2, num + tree[pos + 1], tree)
    else:
        if pos == 1: return
        else: change((pos - 1) // 2, num + tree[pos - 1], tree)
for i in range(n): change(i_to_n(i, n), arr[i], tree)
print(tree)
    



