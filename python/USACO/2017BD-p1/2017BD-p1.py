lines = open('billboard.in', 'r').read().strip().split('\n')
b1, b2, truck = list(map(int, lines[0].split(' '))), list(map(int, lines[1].split(' '))), list(map(int, lines[2].split(' ')))
max_x, max_y = max(b1[0], b1[2], b2[0], b2[2]), max(b1[1], b1[3], b2[1], b2[3])
min_x, min_y = min(b1[0], b1[2], b2[0], b2[2]), min(b1[1], b1[3], b2[1], b2[3])
space = [[0] * (max_x - min_x + 1) for i in range(max_y - min_y + 1)]

for x1 in range(b1[0] + 1000, b1[2] + 1000):
	for y1 in range(b1[1] + 1000, b1[3] + 1000):
		space[x1][y1] += 1
		
for x2 in range(b2[0] + 1000, b2[2] + 1000):
	for y2 in range(b2[1] + 1000, b2[3] + 1000):
		space[x2][y2] += 1

total_board = 0
for x in range(min_x + 1000, max_x + 1001):
	for y in range(min_y + 1000, max_y + 1001):
		if space[x][y] == 1: total_board += 1

for x3 in range(truck[0] + 1000, truck[2] + 1000):
	for y3 in range(truck[1] + 1000, truck[3] + 1000):
		space[x3][y3] += 1

overlapped = 0
for x in range(min_x + 1000, max_x + 1001):
	for y in range(min_y + 1000, max_y + 1001):
		if space[x][y] == 2: overlapped += 1

print(total_board - overlapped)
file = open('billboard.out', 'w')
file.write(str(total_board - overlapped))
file.close()

