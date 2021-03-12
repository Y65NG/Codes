import sys

lines = sys.stdin.read().strip().split('\n')
M, N, K = [int(x) for x in lines[:3]]
rows, columns = [], []
for i in range(3, 3 + K):
    line = lines[i].split(' ')
    if line[0] == 'R': rows.append(int(line[1]))
    else: columns.append(int(line[1]))
print(M, N, K, rows, columns)

