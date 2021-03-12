import sys

lines = sys.stdin.read().strip().split('\n')
M, N, K = [int(x) for x in lines[:3]]
rows, columns = [0] * M, [0] * N
grids = [[0] * N for i in range(M)]
g_num = 0
for i in range(3, 3 + K):
    line = lines[i].split(' ')
    
    if line[0] == 'R': 
        rows[int(line[1])] += 1
    else: 
        columns[int(line[1])] += 1
# print(M, N, K, rows, columns, grids)

for r in range(M):
    for c in range(N):
        total = rows[r] + columns[c]
        if total % 2 != 0: g_num += 1
print(g_num)

