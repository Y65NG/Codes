from collections import deque
# 递归
def dfs(u):
    visited = []
    neighbors = []
    if u not in visited: 
        visited.append(u)
        for v in neighbors[u]: dfs(v)
    return visited

# 迭代
def dfs2(u):
    frontier = deque()
    todo = []
    frontier.push(u)
    todo.append(u)
    while len(frontier) > 0:
        nodes = frontier.pop()
        for node in nodes.neighbors:
            if node not in todo:
                todo.append(node)
                frontier.append(node)
