def next(pos):
	global cows
	if pos == 0: return pos + 1
	if pos == len(cows) - 1: return pos - 1
	if cows[pos - 1] <= cows[pos + 1]: return pos - 1
	else: return pos + 1

def largest_interval():
	global diffs
	max_index = 0
	for i in range(len(diffs)):
		if diffs[i] >= diffs[max_index]: max_index = i
	return max_index

def process():
	global cows
	count = 0
	
	

lines = open('hoofball.in').read().strip().split('\n')
n = int(lines[0])
cows = list(map(int, lines[1].split(' ')))
cows.sort()
diffs = []
for i in range(len(cows) - 1):
	diffs.append(cows[i + 1] - cows[i])


