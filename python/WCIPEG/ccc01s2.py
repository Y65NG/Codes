def move(dir, coor):
    if dir == 0: return (coor[0], coor[1] + 1)
    if dir == 1: return (coor[0] - 1, coor[1])
    if dir == 2: return (coor[0], coor[1] - 1)
    if dir == 3: return (coor[0] + 1, coor[1])

x = int(input())
y = int(input())
total = y - x + 1
width = int(total ** 0.5)
graph = [[0] * 11 for _ in range(11)]
direct = 0 # 0为右，逆时针
step = 2
graph[5][5] = x
coor = (6, 5)
num = x + 1
while num < y + 1:
    
    graph[coor[0]][coor[1]] = num
    # print(num)
    # print(graph)
    if (num - x) % step == 0: 
        if direct == 3: direct = 0
        else: direct += 1
    coor = move(direct, coor)
    num += 1
    
    if num == x + step * 4: step += 2
print(graph)

