lines = open('planting.in').read().strip().split('\n')
n = int(lines[0])
edges = {}
colors = {}
num = 0

for i in range(1, n):
	line = list(map(int, lines[i].split(' ')))
	if line[0] not in edges: edges[line[0]] = [line[1]]
	else: edges[line[0]].append(line[1])
	if line[1] not in edges: edges[line[1]] = [line[0]]
	else: edges[line[1]].append(line[0])
	
max_value = 0	
for value in edges.items():
	if len(value[1]) > max_value:
		max_value = len(value[1])
print(max_value + 1)
file = open('planting.out', 'w')
file.write(str(max_value + 1))
file.close()
