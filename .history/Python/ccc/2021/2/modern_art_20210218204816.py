import sys

lines = sys.stdin.read().strip().split('\n')
M, N, K = [int(x) for x in lines[:3]]
act_rows, act_columns = {}, {}

for i in range(3, 3 + K):
    line = lines[i].split(' ')
    if line[0] == 'R': 
        if line[1] not in act_rows: act_rows[line[1]] = 1
        else: act_rows[line[1]] += 1
    else: 
        if line[1] not in act_columns: act_columns[line[1]] = 1
        else: act_columns[line[1]] += 1
print(M, N, K, act_rows, act_columns)



