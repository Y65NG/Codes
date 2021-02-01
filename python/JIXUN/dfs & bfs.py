data = list(map(int, input().split(' ')))
N, E = data[0], data[1]
edges = []
count = 0
def dfs(u, visited, neighbor):
    if u not in visited: 
        
        # print(neighbor[u])
        for v in neighbor: dfs(v, visited, neighbor)
    
        return visited
graph = {}

while True:
    line = input()
    if line == '': break
    points = list(map(int, line.split(' ')))
    if points[0] not in graph: graph[points[0]] = [points[1]]
    else: graph[points[0]].append(points[1])
    if points[1] not in graph: graph[points[1]] = [points[0]]
    else: graph[points[1]].append(points[0])

point = 0
while point <= N:
    print(dfs(point, [], graph[point]))
    point = max(dfs(point, [], graph[point])) + 1
    count += 1

# data = list(map(int, input().split()))
