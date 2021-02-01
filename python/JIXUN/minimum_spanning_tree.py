import heapq
# Kruskal's
parents = []
points = []
edges = []
def root(u):
    global parents
    while parents[u] != None: u = parents[u]
    return u
#
def union(u, v):
    global parents
    if root(u) != root(v): parents[u] = v

def find(u, v):
    return root(u) == root(v)

while True:
    data = list(map(int, input().split(' ')))
    edges = []
    mst = []
    for _ in range(data[1]):
        line = list(map(int, input().split(' ')))
        heapq.heappush(edges, (line[2],line[0],line[1]))
    # print(edges)
    while len(edges) > 0:
        edge = heapq.heappop(edges)
        print(edge)
        print(find(edge[1], edge[2]))
        if not find(edge[1], edge[2]):
            mst.append((edge[1],edge[2]))
            union(edge[1], edge[2])
            print(mst)

# Prim's
data = list(map(int, input().split(' ')))
n, l = data[0], data[1]
graph = [{} for _ in range(n)]
dist = [float('inf')] * n

children = [-1] * n

visited = [False] * n
# weight = 
for _ in range(l):
    line = list(map(int, input().split(' ')))
    graph[line[0]][line[1]] = line[2]
    graph[line[1]][line[0]] = line[2]


def find_min_dist_index():
    global dist
    val = float('inf')
    index = -1
    for i in range(len(dist)):
        if not visited[i] and dist[i] < val:
            val = dist[i]
            index = i
    return index

def mst():
    global n, l, graph, dist, children
    dist[0] = 0
    children[0] = 0
    for i in range(n):
        u = find_min_dist_index()
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                if graph[u][v] < dist[v]:
                    dist[v] = graph[u][v]
                    children[v] = u

mst()
print(dist)
print(children)
