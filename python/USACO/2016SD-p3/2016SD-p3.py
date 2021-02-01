def distance(p1, p2):
	return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
	
def neighbors(pos):
	global poses, powers
	
	result = set()
	for i in range(len(poses)):
		if i == pos: continue
		if distance(poses[pos], poses[i]) <= powers[pos]: result.add(i)
	return result

def process(pos):
	global poses, visited
	
	visited.add(pos)
	neighbor_pos = neighbors(pos)
	#print(neighbor_pos)
	if len(neighbor_pos) == 0: return
	for neighbor in neighbor_pos:
		if neighbor not in visited: process(neighbor)

lines = open('moocast.in').read().strip().split('\n')
n = int(lines[0])
poses = []
powers = []

for i in range(1, n + 1):
	line = list(map(int, lines[i].split(' ')))
	pos = (line[0], line[1])
	power = line[2]
	poses.append(pos)
	powers.append(power)

max_size = 0
for i in range(len(poses)):
	visited = set()
	process(i)
	max_size = max(len(visited), max_size)

print(max_size)
file = open('moocast.out', 'w')
file.write(str(max_size))
file.close()
	
