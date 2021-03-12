import sys

def addWeight(x, y):
    global weights
    weights[x][y + 1] += 1
    weights[x + 2][y + 1] += 1
    weights[x + 1][y] += 1
    weights[x + 1][y + 2] += 1

def addACow(x, y):
    global cows
    judge = False
    if cows[x + 1][y + 1] != 0: judge = True
    cows[x + 1][y + 1] = 1
    addWeight(x, y)
    return judge
    
def detectWeight(x, y): # 返回 weight 为 3 的位置
    global weights
    if weights[x][y + 1] == 3 and cows[x][y + 1] != 0: return (x - 1, y)
    elif weights[x + 2][y + 1] == 3 and cows[x + 2][y + 1] != 0: return (x + 1, y)
    elif weights[x + 1][y] == 3 and cows[x + 1][y] != 0: return (x, y - 1)
    elif weights[x + 1][y + 2] == 3 and cows[x + 1][y + 2] != 0: return (x, y + 1)
    return (-1, -1)

def detectCow(x, y): 
    global cows
    if x != 0 and cows[x][y + 1] == 0: return (x - 1, y)
    elif x != 1004 and cows[x + 2][y + 1] == 0: return (x + 1, y)
    elif y != 0 and cows[x + 1][y] == 0: return (x, y - 1)
    elif y != 1004 and cows[x + 1][y + 2] == 0: return (x, y + 1)

lines = sys.stdin.read().strip().split('\n')
# lines = open('test.txt').read().strip().split('\n')
N = int(lines[0])
cows = [[0] * 1005 for i in range(7)]
weights = [[0] * 1005 for i in range(7)]
num = 0
for i in range(1, N + 1):
    print('i:', i)
    x, y = [int(x) for x in lines[i].split(' ')]
    judge = addACow(x, y)
    if judge: num -= 1
    
    
    while detectWeight(x, y) != (-1, -1):
        weightPos = detectWeight(x, y)
        cowPos = detectCow(weightPos[0], weightPos[1])
        addACow(cowPos[0], cowPos[1])
        num += 1
        x, y = cowPos
    print(num)
    
