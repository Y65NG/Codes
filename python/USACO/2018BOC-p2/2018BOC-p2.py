lines = open('milkorder.in').read().strip().split('\n')
n, m, k = list(map(int, lines[0].split(' ')))
order = list(map(int, lines[1].split(' ')))
pos_cow = {}
for i in range(2, k + 2):
	line = list(map(int, lines[i].split(' ')))
	pos_cow[line[0]] = line[1]

pos = [0] * (n + 1)

for i in pos_cow:
	pos[pos_cow[i]] = i

if 1 in order:
	cur = 1
	for num in range(0, len(order)):
		if order[num] in pos:
			cur = pos.index(order[num]) + 1
		else:
			for i in range(cur, len(pos)):
				if pos[i] == 0:
					pos[i] = order[num]
					cur = i + 1
					break
else:
	cur = len(pos) - 1
	for num in range(len(order) - 1, -1, -1):
		if order[num] in pos:
			cur = pos.index(order[num]) - 1
		else: 
			for i in range(cur, 0, -1):
				if pos[i] == 0: 
					pos[i] = order[num] 
					cur = i - 1
					break
#print(pos)

file = open('milkorder.out', 'w')
if 1 in pos: 
	file.write(str(pos.index(1)))
	print(pos.index(1))
else:
	for i in range(1, len(pos)):
		if pos[i] == 0:
			print(i)
			file.write(str(i))
			break

file.close()

