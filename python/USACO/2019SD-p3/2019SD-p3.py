def root(u, parents):
    while parents[u] != u: u = parents[u]
    return u

def union(u, v, parents):
    if root(u, parents) != root(v, parents):
        parents[root(v, parents)] = root(u, parents)

def find(u, v, parents):
    return root(u, parents) == root(v, parents)

lines = open('milkvisits.in').read().strip().split('\n')
n, m = list(map(int, lines[0].split(' ')))
G = list(range(n + 1))
H = list(range(n + 1))

cows = list(lines[1])
for i in range(2, n + 1):
	line = list(map(int, lines[i].split(' ')))
	#print(line)
	if cows[line[0] - 1] == cows[line[1] - 1]: 
		if cows[line[0] - 1] == 'H': union(line[0], line[1], H)
		else: union(line[0], line[1], G)
#print(G,H)

result = ''
for i in range(n + 1, n + m + 1):
	line = lines[i].split(' ')
	u, v = list(map(int, line[:-1]))
	cow = line[-1]
	if u == v: 
		if cow == cows[u - 1]: result += '1'
		else: result += '0'
	elif find(u, v, H):
		if cow == 'H': result += '1'
		else: result += '0'
	elif find(u, v, G):
		if cow == 'G': result += '1'
		else: result += '0'
	else: result += '1'
print(result)

file = open('milkvisits.out', 'w')
file.write(str(result))
file.close()
