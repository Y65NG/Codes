import heapq
data = list(map(int, input().split(' ')))
graph = [[] for _ in range(data[0])]
dist = [float('inf')] * data[0]
pq = []
for _ in range(data[1]):
    line = list(map(int, input().split(' ')))
    graph[line[0]].append((line[2], line[1]))
    graph[line[1]].append((line[2], line[0]))

def neighbors(u):
    result = []
    for i in graph[u]:
        result.append(i[1])
    return result

def weight(u, v):
    for i in graph[u]:
        if i[1] == v: return i[0]

def diikstra(u, v):
    global graph, dist, pq
    heapq.heappush(pq, (0, u))
    while len(pq) > 0:
        # print(dist)
        cost, w = heapq.heappop(pq)
        if w == v: return cost
        for x in neighbors(w):
            heapq.heappush(pq, (cost + weight(w, x), x))
    # return dist[v]
print(diikstra(8,4))