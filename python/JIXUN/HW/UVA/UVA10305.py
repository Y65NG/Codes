from collections import deque
while True:
    data = input()
    if data == '0 0': break
    n, m = int(data.split(' ')[0]), int(data.split(' ')[1])
    frontier = deque()
    in_degree = [-1] + [0] * (n)
    graph = [[] for i in range(n + 1)]
    result = []
    for _ in range(m):
        line = list(map(int, input().split(' ')))
        graph[line[0]].append(line[1])
        in_degree[line[1]] += 1
    for i in range(len(in_degree)):
        if in_degree[i] == 0: 
            frontier.append(i)
            result.append(i)
    while len(frontier) > 0:
        next = frontier.pop()
        for task in graph[next]:
            in_degree[task] -= 1
            if in_degree[task] == 0: 
                frontier.append(task)
                result.append(task)
    for i in range(len(result)):
        print(result[i], end = ' ')
    print()
