from collections import deque
f = open()

for row in range(line[0]):
    graph = []
    graph.append(input())

visited = set()
count = 0

def valid(x, y):
    return x >= 0 and y >= 0 and x < len(graph[0]) and y < len(graph) and graph[y][x] == '#'

def neighbors(x, y):
    result = set()
    # print(x,y)
    for diffx in range(-1, 2):
        for diffy in range(-1, 2):
            if (diffx != 0 or diffy != 0) and not(diffx == diffy or diffx == -diffy) and valid(x, y): result.add((x + diffx, y + diffy))
    
    return result
def dfs(x, y):
    # print(x,y)
    frontier = deque()
    todo = set()
    frontier.append((x, y))
    todo.add((x, y))
    while len(frontier) > 0:
        coor = frontier.pop()
        for point in neighbors(coor[0], coor[1]):
            if point not in todo:
                todo.add(point)
                frontier.append(point)
                visited.add(point)
    
for y in range(len(graph)):
    for x in range(len(graph[0])):
        if graph[y][x] == '#' and (x, y) not in visited:
            # print(x,y)
            dfs(x, y)
            count += 1
            # print(count)
print(count)

