import sys

lines = sys.stdin.read().strip().split('\n')
M, N, K = [int(x) for x in lines[:3]]
act_rows, act_columns = [0] * M, [0] * N
grids = [[0] * N for i in range(M)]

for i in range(3, 3 + K):
    line = lines[i].split(' ')
    
    if line[0] == 'R': 
        act_rows[int(line[1])] += 1
    else: 
        act_columns[int(line[1])] += 1
print(M, N, K, act_rows, act_columns, grids)

# for i in range(act_rows):
