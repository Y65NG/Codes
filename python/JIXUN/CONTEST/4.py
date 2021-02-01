import heapq
def change(letter):
    return ord(letter) - ord('A')

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
    total = 0
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

while True:
    N = int(input())
    if N == 0: break
    edges = []
    points = []
    parents = list(range(N))
    for _ in range(N - 1):
        line = input().split(' ')
        k = int(line[1])
        for j in range(2, 2 * k + 1):
            if j % 2 == 0:
                heapq.heappush(edges, (int(line[j + 1]), change(line[0]), change(line[j])))
    print(kruskal())

