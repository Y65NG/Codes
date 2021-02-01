def match(city, code):
	if city[:2] == code: return True
	return False

lines = open('citystate.in').read().strip().split('\n')
n = int(lines[0])
pairs = {}
visited = {}
for i in range(1, n + 1):
	line = lines[i].split(' ')
	if line[1] not in pairs: pairs[line[1]] = {line[0]}
	else: pairs[line[1]].add(line[0])
print(pairs)

for pair in pairs.items():
	if pair[0][:2] not in visited: >
	for city in pair[1]:
		if city[:2] in pairs 
