n = int(input())
arr = [int(x) for x in input().split(' ')]
if n % 2 == 0:
    tree = [0] * n # 第 0 位空着
    tree += arr
else: 
    tree = [0] * (n + 1)
    tree += arr + [0]

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
    



