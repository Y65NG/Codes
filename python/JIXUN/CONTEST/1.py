import sys
from collections import deque
lines = sys.stdin.read().strip().split('\n')
#rint(lines)
def neighbors(index, board):
    result = []
    for i in range(index + 1, len(board) - 1):
        if board[i] > board[index]: result.append(i)
    return result

# move: index 到 end 的最高分
def move(index, board):
    if index == len(board) - 1: return 0
    max = 0
    for next in neighbors(index, board):
        point = move(next, board)
        if point > max: max = point
    if index == 0: total = max
    else: total = board[index] + max
    return total
for _ in range(len(lines) - 1):
    line = list(map(int, lines[_].split(' ')))
    N = line[0]
    board = [-float('inf')] + line[1:] + [float('inf')]
    print(move(0, board))
