lines = open('billboard.in', 'r').read().strip().split('\n')
space = {}
b1, b2, truck = list(map(int, lines[0].split(' '))), list(map(int, lines[1].split(' '))), list(map(int, lines[2].split(' ')))

for x1 in range(b1[0], b1[2]):
	for y1 in range(b1[1], b1[3]):
		space[(x1, y1)] = 1
		
for x2 in range(b2[0], b2[2]):
	for y2 in range(b2[1], b2[3]):
		space[(x2, y2)] = 1

total_board = len(space)
overlapped = 0
for x3 in range(truck[0], truck[2]):
	for y3 in range(truck[1], truck[3]):
		if (x3, y3) in space: 
			#space[(x3, y3)] += 1
			overlapped += 1

#overlapped = 0
#for i in space.values():
#	if i == 2: overlapped += 1

print(total_board - overlapped)
file = open('billboard.out', 'w')
file.write(str(total_board - overlapped))
file.close()
