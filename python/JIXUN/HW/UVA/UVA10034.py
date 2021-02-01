import heapq
time = int(input())

edges = []
parents = []
points = []


def generate_edges():
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            heapq.heappush(edges, (distance(points[i], points[j]), i, j))

def distance(u, v):
    # print(((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5)
    # print(u, v)
    return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5

    
def root(u):
    global parents
    while parents[u] != u: u = parents[u]
    return u

def union(u, v):
    global parents
    #if root(u) != root(v): parents[v] = u
    if root(u) != root(v):
        parents[root(v)] = root(u)

def find(u, v):
    return root(u) == root(v)

def kruskal():
    total = 0.0
    for i in range(len(edges)):
        e = heapq.heappop(edges)
        weight = e[0]
        u = e[1]
        v = e[2]
        if not find(u, v):
            union(u, v)
            total+= weight
            # print(weight)
    return total


for _ in range(time):
    input()
    n = int(input())
    points = []
    parents = list(range(n))
    edges = []
    for __ in range(n):
        line = list(map(float, input().split(' ')))
        points.append((line[0], line[1]))
    generate_edges()
    # print(edges)
    # print(points)
    ans = kruskal()
    print(str('%.2f'% ans))
    if _ != time - 1:print()
'''
parents = [0, 1 ,1, 2, 3]
print(root(2), root(3), root(4))
'''
