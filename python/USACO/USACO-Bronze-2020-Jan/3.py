n = int(input())
cows = []
for i in range(1, n + 1):
	line = input().split(' ')
	dir = line[0]
	pos = tuple(map(int, line[1:]))
	cows.append((i - 1, dir, pos))

times = [-1] * n
stopped_x = {}
stopped_y = {}

cows_x = sorted(cows, key = lambda x: x[2][0])
cows_y = sorted(cows, key = lambda x: x[2][1])

# Transverse North cows
for y in range(n):
	c1 = cows_x[y]
	x1, y1 = c1[2]
	if c1[1] == 'N':
		for x in range(n):
			c2 = cows_y[x]
			x2, y2 = c2[2]
			if (c2[0] not in stopped_x or stopped_x[c2[0]] > x1) and c2[1] == 'E' and x1 - x2 > 0 and y2 - y1 > 0:
				dx, dy = x1 - x2, y2 - y1
				if dx < dy: 
					stopped_y[c1[0]] = y2
					times[c1[0]] = dy
					break
				elif dx > dy:
					stopped_x[c2[0]] = x2
					times[c2[0]] = dx

for i in times:
	if i == -1: print('Infinity')
	else: print(i)
