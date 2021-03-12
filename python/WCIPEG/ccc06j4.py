import sys, time
lines = [int(x) for x in sys.stdin.read().strip().split('\n')[:-2]]
tasks = [None,{2},set(),set(),{1,3},{3},set(),{1}]
# print(lines)
# print(tasks)
index = 0
while index < len(lines) - 1:
    tasks[lines[index + 1]].add(lines[index])
    index += 2
# print(tasks)

result = []
visited = set()
while len(visited) < 7:
    for task in range(1, len(tasks)):
        if task not in visited and tasks[task].issubset(visited): 
            result.append(task)
            visited.add(task)
            # for i in tasks:
            #     if i is not None and task in i: i.remove(task)
            break
for i in result:
    print(i, end = ' ')
    # time.sleep(1)