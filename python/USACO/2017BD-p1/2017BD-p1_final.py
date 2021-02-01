lines = open('billboard.in', 'r').read().strip().split('\n')

b1, b2, truck = list(map(int, lines[0].split(' '))), list(map(int, lines[1].split(' '))), list(map(int, lines[2].split(' ')))

total_board = (b1[2] - b1[0]) * (b1[3] - b1[1]) + (b2[2] - b2[0]) * (b2[3] - b2[1])
overlapped = 0
for x3 in range(truck[0], truck[2]):
	for y3 in range(truck[1], truck[3]):
		if (b1[0] <= x3 <= b1[2] - 1 and b1[1] <= y3 <= b1[3] - 1) or (b2[0] <= x3 <= b2[2] - 1 and b2[1] <= y3 <= b2[3] - 1):
			overlapped += 1

print(total_board - overlapped)
file = open('billboard.out', 'w')
file.write(str(total_board - overlapped))
file.close()
