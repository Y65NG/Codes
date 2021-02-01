def valid(mid):
	global times, n, m, c
	
	index = 0
	bus = 0
	num = 0
	timespan = times[0] + mid
	
	while index < n and bus < m:
		 if num < c and times[index] <=	timespan:
		 	index += 1
		 	num += 1
		 else:
		 	timespan = times[index] + mid
		 	num = 0
		 	bus += 1
		 	
	return index > n - 1
		
	
lines = open('convention.in').read().strip().split('\n')
n, m, c = list(map(int, lines[0].split(' ')))

times = sorted(list(map(int, lines[1].split(' '))))
high = max(times) - min(times)
low = -1
while high - low > 1:
	mid = (high + low) // 2
	if valid(mid): high = mid
	else: low = mid

print(high)
file = open('convention.out', 'w')
file.write(str(high))
file.close()
