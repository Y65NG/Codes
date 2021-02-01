from collections import deque
c = int(input())
for _ in range(c):
    data = input().split(' ')
    n, t, m = int(data[0]), int(data[1]), int(data[2])
    side = 0
    time = 0
    left = deque()
    right = deque()
    for __ in range(m):
        line = input().split(' ')
        if line[1] == 'left': left.append(int(line[0]))
        else: right.append(int(line[0]))
        
    