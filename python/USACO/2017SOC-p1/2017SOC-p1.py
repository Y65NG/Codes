lines = open('pairup.in').read().strip().split('\n')
n = int(lines[0])
cows = []
for i in range(1, n + 1):
	line = list(map(int, lines[i].split(' ')))
	cows.append([line[1], line[0]])
cows.sort()
# print(cows)

max_times = 0
left = 0
right = len(cows) - 1
while left <= right:
	max_t, max_n = cows[right]
	min_t, min_n = cows[left]
	# print(cows, max_cow, min_cow)
	if max_n == min_n:
		cows[right][1] = 0
		cows[left][1] = 0
	else:	
		if max_n >= min_n:
			cows[right][1] -= min_n
			cows[left][1] -= min_n
		elif max_n < min_n:
			cows[right][1] -= max_n
			cows[left][1] -= max_n
	max_times = max(max_times, max_t + min_t)
	
	if cows[right][1] == 0:
		right -= 1
	
	elif cows[left][1] == 0:
		left += 1
print(max_times)
fout = open('pairup.out', 'w')
fout.write(str(max_times))
fout.close()