def find_intervals(ci, dir): # find all intervals of ci and cj
	global cows
	
	

lines = open('6.in').read().strip().split('\n')
n = int(lines[0])
#n = int(input())
cows = []
for i in range(1, n + 1):
	line = lines[i].split(' ')
	dir = line[0]
	pos = tuple(map(int, line[1:]))
	cows.append((i - 1, dir, pos))

times = []
intervals = []
for i in range(n): 
	cow = cows[i]
	x1, y1 = cow[2]
	dir = cow[1]
	intervals += find_intervals(i, dir)

intervals.sort()

	
