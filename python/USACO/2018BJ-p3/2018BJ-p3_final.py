def bessie(cows):
	for i in range(0, len(cows)):
		if i == 0:
			if cows[i] > cows[i + 1]: 
				#print('a')
				return i
		elif i == len(cows) - 1: 
			if cows[i] < cows[i - 1]: 
				#print('b')
				return i
	for i in range(1, len(cows) - 1):
		if cows[i] < cows[i - 1] <= cows[i + 1] or cows[i] > cows[i + 1] >= cows[i - 1]: 
			#print('c', i, cows[i])
			return i
	return -1

def origin(cows, pos):
	bessie = cows[pos]
	#print(pos, bessie)
	dir = False
	for i in range(len(cows)):
		#print(i)
		if i < pos:
			#print('not')
			if bessie < cows[i]: 
				#print('not', bessie, cows[i], i)
				return i
		if i > pos:
			if bessie <= cows[i]: 
				#print(bessie, cows[i], i)
				return i
	#print('not')


def process(cows):
	cur_pos = bessie(cows)
	if cur_pos == -1: return 0
	else:
		step = 0
		ori_pos = origin(cows, cur_pos)
		count = 0
		if ori_pos < cur_pos:
			for i in range(cur_pos, ori_pos, -1):
				if cows[i] != cows[i - 1]:
					#print(i)
					count += 1
		else:
			for i in range(cur_pos, ori_pos - 1):
				if cows[i] != cows[i + 1]:
					#print(i)
					count += 1
	#print(cur_pos, ori_pos, cows)
	return count
				
			

lines = open('outofplace.in').read().strip().split('\n')
n = int(lines[0])
cows = list(map(int, lines[1:]))
result = process(cows)
print(result)
file = open('outofplace.out', 'w')
file.write(str(result))
file.close()

