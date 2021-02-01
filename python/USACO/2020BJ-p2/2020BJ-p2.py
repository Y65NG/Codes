def valid(start):
	global bcows
	visited = set()
	acows = [start]
	for i in range(len(bcows)):
		next = bcows[i] - acows[i]
		if next in visited: return False, acows
		visited.add(next)
		acows.append(next)
	return True, acows
		
lines = open('photo.in').read().strip().split('\n')
#n, bcows = int(lines[0]), list(map(int, lines[1].split(' ')))
n, bcows = int(lines[0]), [int(i) for i in lines[1].split(' ')]

result = ''
for i in range(1, n + 1):
	test = valid(i)
	if test[0]: 
		acows = test[1]
		for acow in acows: result += str(acow) + ' '
		break

print(result)
file = open('photo.out', 'w')
file.write(result.strip())
file.close()
