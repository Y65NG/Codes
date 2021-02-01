def bessie_pos(cows):
	for i in range(1, len(cows)):
		if cows[i] < cows[i - 1]: return i
	return -1

def duplicate_areas(cows, dir):
	duplicate = {}
	if dir:
		for i in range(len(cows) - 1):
			for j in range(i + 1, len(cows)):
				if cows[j] == cows[i]:
					if i not in duplicate: duplicate[i] = 2
					else: duplicate[i] += 1
				else: break
	else:
		#print('Yes')
		for i in range(len(cows) - 1, 0, -1):
			for j in range(i - 1, -1, -1):
				if cows[j] == cows[i]:
					#print('Yes')
					if i not in duplicate: duplicate[i] = 2
					else: duplicate[i] += 1
				else: break
	return duplicate

def swap(pos1, pos2):
	global cows
	cows[pos1], cows[pos2] = cows[pos2], cows[pos1]

filein = open('outofplace.in').read().strip().split('\n')
n = int(filein[0])
cows = list(map(int, filein[1:]))
count = 0
#print(duplicate_areas(cows, True))
if bessie_pos(cows) != -1: 
	pos = bessie_pos(cows)
	dir = True
	if pos != 0 and cows[pos - 1] > cows[pos]: dir = False
	duplicate = duplicate_areas(cows, dir)
	#print(duplicate)
	if dir:

		while pos < len(cows) - 2:
			#print(pos)
			step = 1
			if pos in duplicate: step = duplicate[pos]
			if cows[pos + step] < cows[pos]: 
				#print(pos)
				swap(pos, pos + step)
				pos += step
				count += 1
			
	else:
		while pos > 1:
			#print(pos)
			step = 1
			if pos in duplicate: step = duplicate[pos]
			if cows[pos - step] > cows[pos]: 
				#print(pos)
				swap(pos, pos - step)
				pos -= step
				count += 1
print(count)
fileout = open('outofplace.out', 'w')
fileout.write(str(count))
fileout.close()
