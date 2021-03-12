import sys

def switch(start):
    f = [0] * 100010
    count = start
    while count != f[count]: count = f[count]
    num = start
    while num != count: 
        index = f[num]
        f[num] = count
        num = index
    return count

def fun(arr, n):
    result = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            result += arr[i][j]
    return result

def c2(x):
    return (x + 1) * x // 2

def cal(arr, n):
    global pairs
    arr[n + 1] = -1
    count = 0
    l = 1
    for i in range(1, n + 2):
        if arr[i] < 100:
            pairs[count + 1] = (l, i - 1)
            l = i + 1
    ret = 0
    for i in range(1, count + 1):
        l, r = pairs[i]
        if l > r: continue
        num = r - l + 1
        tot = c2(num)
        memo = arr[r + 1]
        arr[r + 1] = 100
        ll = l - 1
        for j in range(l, r + 2):
            if arr[j] == 100:
                tot -= c2(j - ll - 1)
                ll = j
        arr[r + 1] = memo
        ret += tot
    return ret



lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
grids = []
for i in range(1, N + 1):
    line = [int(x) for x in lines[i].split(' ')]
    grids.append(line)
# print(grids)
pairs = [0] * N
numList = []
arr = [[0] * N for i in range(N)]
for up in range(1, N + 1):
    numlist = [0x3f3f3f3f] * N
    for down in range(up, N + 1):
        for i in range(1, N + 1):
            numlist[i] = min(numlist[i], grids[down][i])
        arr[up]

