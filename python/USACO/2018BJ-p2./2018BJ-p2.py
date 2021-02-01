def fire(pos):
	global timestamp, times
	time = times[pos]
	temp = timestamp.copy()
	for i in range(time[0], time[1]):
		temp[i] -= 1
	
	count = 0
	for i in temp.values():
		if i != 0: count += 1
	return count
	


lines = open('lifeguards.in').read().strip().split('\n')
n = int(lines[0])
timestamp = {}
times = []
for i in range(1, n + 1):
	time = tuple(map(int, lines[i].split(' ')))
	times.append(time)
	for j in range(time[0], time[1]):
		if j not in timestamp: timestamp[j] = 1
		else: timestamp[j] += 1
		
max_count = fire(0)
for i in range(1, len(times)):
	count = fire(i)
	if count > max_count: max_count = count

print(count)
file = open('lifeguards.out', 'w')
file.write(str(count))
file.close()
#print(timestamp)

