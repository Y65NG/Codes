from collections import deque
triangle = [
    [-1],
    [2,3],
    [1,-1,-3]
]
def neighbors(u, triangle):
    return [(u[0] + 1, u[1]), (u[0] + 1, u[1] + 1)]

def minimumTotal(triangle):
    for x in range(len(triangle) - 2, -1, -1):
        for y in range(len(triangle[x])):
            next = neighbors((x, y), triangle)
            triangle[x][y] += min(triangle[next[0][0]][next[0][1]], triangle[next[1][0]][next[1][1]])
    return triangle[0][0]

print(minimumTotal(triangle))

