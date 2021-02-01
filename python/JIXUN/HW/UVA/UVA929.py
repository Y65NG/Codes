import heapq
def diikstra(u, v):
    global N, M, cost_maze
    heapq.heappush(pq, (cost_maze[0][0], u))
    while len(pq) > 0:
        cost, w = heapq.heappop(pq)
        if w == v: return cost
        for x in neighbors(w):
            if x not in visited:
                heapq.heappush(pq, (cost + weights(x), x))
                visited.add(x)

def weights(v):
    # print(v[0], v[1])
    return cost_maze[v[0]][v[1]]

def neighbors(u):
    result = []
    x = u[0]
    y = u[1]
    for next in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= next[0] < N and 0 <= next[1] < M:
            result.append(next)
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    cost_maze = []
    pq = []
    visited = set()
    for __ in range(N):
        cost_maze.append(list(map(int, input().split(' '))))

    print(diikstra((0,0),(N - 1, M - 1)))
    