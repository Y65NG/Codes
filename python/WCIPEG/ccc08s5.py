n = int(input())
reactions = [[2,1,0,2], [1,1,1,1], [0,0,2,1], [0,3,0,0], [1,0,0,1]]
cache = {}
# 返回当前 state 所有能反应的下一个 state
def canReact(state):
    newState = []
    if state[0] >= reactions[0][0] and state[1] >= reactions[0][1] and state[2] >= reactions[0][2] and state[3] >= reactions[0][3]:
        newState.append([state[0] - reactions[0][0], state[1] - reactions[0][1], state[2] - reactions[0][2], state[3] - reactions[0][3]])
    if state[0] >= reactions[1][0] and state[1] >= reactions[1][1] and state[2] >= reactions[1][2] and state[3] >= reactions[1][3]:
        newState.append([state[0] - reactions[1][0], state[1] - reactions[1][1], state[2] - reactions[1][2], state[3] - reactions[1][3]])
    if state[0] >= reactions[2][0] and state[1] >= reactions[2][1] and state[2] >= reactions[2][2] and state[3] >= reactions[2][3]:
        newState.append([state[0] - reactions[2][0], state[1] - reactions[2][1], state[2] - reactions[2][2], state[3] - reactions[2][3]])
    if state[0] >= reactions[3][0] and state[1] >= reactions[3][1] and state[2] >= reactions[3][2] and state[3] >= reactions[3][3]:
        newState.append([state[0] - reactions[3][0], state[1] - reactions[3][1], state[2] - reactions[3][2], state[3] - reactions[3][3]])
    if state[0] >= reactions[4][0] and state[1] >= reactions[4][1] and state[2] >= reactions[4][2] and state[3] >= reactions[4][3]:
        newState.append([state[0] - reactions[4][0], state[1] - reactions[4][1], state[2] - reactions[4][2], state[3] - reactions[4][3]])
    return newState

# 判断当前 state 能不能赢
def isWin(state):
    if tuple(state) in cache: return cache[tuple(state)]
    nextState = canReact(state)
    # print(nextState)
    if nextState == []: return False
    for each in nextState:
        if not isWin(each): 
            cache[tuple(state)] = True 
            # print('lose')
            return True
        cache[tuple(state)] = False
    return False
    
    
for a in range(n):
    line = input()
    ABCD = line.split(' ')
    state = []
    for i in ABCD:
        state.append(int(i))
    if isWin(state): print('Patrick')
    else: print('Roland')