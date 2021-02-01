graph = []
dyed = []
visited = []
def dfs(u):
    for v in graph[u]:
        if dyed[v] == None:
            dyed[v] = not dyed[u]
        elif dyed[v] == dyed[u]: return False
        if v not in visited:
            visited.append(v)
            if not dfs(v): return False
    return True
while True:
    n = int(input())
    if n == 0: break
    l = int(input())
    graph = [[] for _ in range(n)]
    visited = []
    dyed = [None] * n
    for _ in range(l):
        line = list(map(int, input().split(' ')))
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    
    dyed[0] = True
    # print(dfs(0))
    if dfs(0): print('BICOLORABLE.')
    else: print('NOT BICOLORABLE.')
