size = input()
n, m = int(size.split(' ')[0]), int(size.split(' ')[1])
room = []
def walls(n):
    wall = ''
    if n - 8 >= 0: 
        wall = '1' + wall 
        n -= 8
    else: wall = '0' + wall
    if n - 4 >= 0:
        wall = '1' + wall 
        n -= 4
    else: wall = '0' + wall
    if n - 2 >= 0:
        wall = '1' + wall 
        n -= 2 
    else: wall = '0' + wall
    if n - 1 >= 0:
        wall = '1' + wall 
        n -= 1
    else: wall = '0' + wall
    return wall

for i in range(m):
    line = input()
    row = []
    for j in range(n):
        # print(row.split(' ')[j])
        row.append(walls(int(line.split(' ')[j])))
    room.append(row)
print(room)