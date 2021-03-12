import sys

def addWeight(x, y):
    global weights
    if x != 0: weights[x][y + 1] += 1
    if x != 1004: weights[x + 2][y + 1] += 1
    if y != 0: weights[x + 1][y] += 1
    if y != 1004: weights[x + 1][y + 2] += 1

def addACow(x, y):
    global cows
    cows[x + 1][y + 1] = 1
    addWeight(x, y)
    
def detect(x, y):
    global weights
    if x != 0 and weights[x][y + 1] == 3 and cows[x][y + 1] != 0: return (x - 1, y)
    elif x != 1004 and weights[x + 2][y + 1] == 3 and cows[x + 2][y + 1] != 0: return (x + 1, y)
    elif y != 0 and weights[x + 1][y] == 3 and cows[x + 1][y] != 0: return (x, y - 1)
    elif y != 1004 and weights[x + 1][y + 2] == 3 and cows[x + 1][y + 2] != 0: return (x, y + 1)
    return (-1, -1)

lines = sys.stdin.read().strip().split('\n')
# lines = open('test.txt').read().strip().split('\n')
N = int(lines[0])
cows = [[0] * 1005 for i in range(1005)]
weights = [[0] * 1005 for i in range(1005)]
for i in range(1, N + 1):
    x, y = [int(x) for x in lines[i].split(' ')]
    addACow(x, y)
    num = 0
    
    while detect(x, y) != (-1, -1):
        pos = detect(x, y)
        addACow(pos[0], pos[1])
        num += 1
        x, y = pos
    print(num)
    
