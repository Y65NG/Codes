grids = []
mem = {}
n = 0
for a in range(10):
    line = input()
    grid = []
    for b in range(9):
        grid.append(line.split(' ')[b])
    grids.append(grid)

# 将序号转换为对应的数字
def change(line):
    global grids
    line = str(line)
    num = 0
    elements = line.split('+')
    global n
    if line == '*': return line
    if line.isdigit(): return line
    if line in mem: return mem[line]
    else:
        for i in elements:
            if (grids[ord(i[0]) - 65][int(i[1:]) - 1]).isdigit():
                corNum = int(grids[ord(i[0]) - 65][int(i[1:]) - 1])
                num += corNum
            else: 
                corLine = grids[ord(i[0]) - 65][int(i[1:]) - 1]
                try:
                    num += int(change(corLine))
                except : 
                    return '*'
                    
                    
    mem[line] = int(num)
    return int(num)
            
for i in range(10):
    for j in range(9):
        grids[i][j] = str(change(grids[i][j]))

print()
for i in range(10):
    for j in range(9):
        print(grids[i][j], end = ' ')
    print()



