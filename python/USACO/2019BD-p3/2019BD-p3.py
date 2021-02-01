import heapq

lines = open('lineup.in').read().strip().split('\n')
n = int(lines[0])
names = [
	'Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue'
]
neighbors = []
visited = set()
for i in range(1, n + 1):
	line = lines[i].split(' ')
	cow1, cow2 = line[0], line[-1]
	visited.add(cow1)
	visited.add(cow2)
	for neighbor in neighbors:
		if cow1 in neighbor:
			if cow2 > cow1 and neighbor.index(cow1) == len(neighbor) - 1:
				neighbor.insert(neighbor.index(cow1) + 1, cow2)
			else:
				neighbor.insert(neighbor.index(cow1), cow2)
			break
		elif cow2 in neighbor:
			if cow1 > cow2 and neighbor.index(cow2) == len(neighbor) - 1:
				neighbor.insert(neighbor.index(cow2) + 1, cow1)
			else:
				neighbor.insert(neighbor.index(cow2), cow1)
			break
	else:
		neighbors.append([cow1, cow2])
print(neighbors)
for neighbor in neighbors:
	neighbor.sort()
neighbors = sorted(neighbors, reverse=True)
print(neighbors)

result = ''
for name in names:
	if name not in visited:
		result += name + '\n'
	else:
		if len(neighbors) != 0:
			for neighbor in neighbors[-1]:
				result += neighbor + '\n'
			neighbors.pop(-1)
print(result)

