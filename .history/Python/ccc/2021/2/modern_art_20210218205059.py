import sys

lines = sys.stdin.read().strip().split('\n')
M, N, K = [int(x) for x in lines[:3]]
act_rows, act_columns = [0] * M, [0] * N
rows, columns = [0] * M, [0] * N

for i in range(3, 3 + K):
    line = lines[i].split(' ')
    
    if line[0] == 'R': 
        act_rows[line[1]] += 1
    else: 
        act_columns[line[1]] += 1
print(M, N, K, act_rows, act_columns)

