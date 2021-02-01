def find(pos, index):
	global spreads
	
	for i in range(index, len(spreads) - 1):
		if spreads[i][1] < pos < spreads[i + 1][0]: return spreads[i + 1][0]
	return pos

def valid(mid):
	global spreads, n, m
	
	index = 0
	pos = spreads[0][0]
	cows = n
	while cows > 0 and pos < spreads[-1][1]:
		#print('pos:', pos)
		new_pos = pos + mid
		if new_pos >= spreads[-1][1]: break
		if new_pos <= spreads[index][1]: pos = new_pos
		elif index == len(spreads) - 1: return False
		else:
			high = len(spreads)
			low = index
#			print(high, low)
			while high - low > 1:
				midd = (high + low) // 2
				#print(high, low, midd)
				if spreads[midd][0] <= new_pos <= spreads[midd][1]:
					pos = new_pos
					break
				elif new_pos < spreads[midd][0]: low = midd
				else: high = midd
			if new_pos < spreads[high][0]: new_pos = spreads[high][0]
		cows -= 1
		
	return cows == 0 
					

lines = open('socdist.in').read().strip().split('\n')
n, m = list(map(int, lines[0].split(' ')))
spreads = []

for i in range(1, m + 1):
	spread = tuple(map(int, lines[i].split(' ')))
	spreads.append(spread)
	
spreads.sort()
print(spreads, spreads[0][0], spreads[-1][1])
high = 10 ** 5 + 1
low = 0
while high - low > 1:
	mid = (high + low) // 2
	is_valid = valid(mid)
	print(mid, is_valid)
	if is_valid: low = mid
	else: high = mid

print(low)
file = open('socdist.out', 'w')
file.write(str(low))
file.close()
