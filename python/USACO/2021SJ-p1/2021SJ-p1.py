# class Node:
#     def __init__(self, value, next):
#         this.value = value
#         this.next = next
import sys  

lines = sys.stdin.read().strip().split('\n')
# print(lines)
N, K = [int(x) for x in lines[0].split(' ')]
cows = [i for i in range(N + 1)]
paths = {}
path_nums = {i:{i} for i in range(1, N + 1)}
# print(path_nums)

for i in range(1, K + 1):
    a, b = [int(x) for x in lines[i].split(' ')]
    # print(a, b)
    path_nums[cows[a]].add(b)
    path_nums[cows[b]].add(a)
    cows[a], cows[b] = cows[b], cows[a]
    
    # print(cows)
    # print(path_nums)

for i in range(1, N + 1):
    paths[cows[i]] = i

# print(paths)

path_nodes = []
visited = set()
index = 0
for i in paths:
    if i not in visited:
        # print(visited)
        
        path_nodes.append({i})
        temp = i 
        while paths[temp] != i:
            visited.add(temp)
            temp = paths[temp] 
            path_nodes[index].add(temp)
        visited.add(temp)
        index += 1
# print(path_nodes)
# print(path_nums)
path_lengths = [i for i in range(N + 1)]
for path in path_nodes:
    visited = set()
    for node in path:
        for num in path_nums[node]:
            visited.add(num)
    # print(visited)
    for node in path:
        path_lengths[node] = len(visited)

for i in range(1, len(path_lengths)):
    print(path_lengths[i])

