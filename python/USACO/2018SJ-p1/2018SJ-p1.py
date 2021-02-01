lines = open('lifeguards.in').read().strip().split('\n')
n = int(lines[0])
shifts = []
times = [0] * 1000

for i in range(1, n + 1):
	line = tuple(map(int, lines[i].split(' ')))
	shifts.append(line)
	for j in range(line[0], line[1]):
		times[j] += 1
#print(times)
max_count = 0
for shift in shifts:
	count = 0
	temp = times.copy()	
	for i in range(shift[0], shift[1]):
		temp[i] -= 1
	for i in temp:
		if i > 0: count += 1
	max_count = max(count, max_count)
print(max_count)

file = open('lifeguards.out', 'w')
file.write(str(max_count))
file.close()
