def check(state, index):
    for i in range(index):
        if state[i] == state[index]: return False # 同一列
        if abs(state[i] - state[index]) == abs(i - index): return False # 同一斜线
    return True
def backtrack(state, n, index): # index: 当前要尝试的位置
    if index == n: # goal
        return 1
    count = 0
    for i in range(n):
        state[index] = i
        if check(state, index): 
            count += backtrack(state, n, index + 1)
    return count
def n_queen(n):
    return backtrack(list(range(n)), n, 0)

print(n_queen(int(input())))
