lines = open('measurement.in', 'r').read().strip().split('\n')
n = int(lines[0])
chrono = []
cows = {}
num_of_change = 0

for i in lines[1:]:
	data = i.split(' ')
	chrono.append((int(data[0]), data[1], data[2]))
	cows[data[1]] = 7
chrono.sort()
print(chrono)
#print(cows)

max_cows = set()

for i in chrono:
	if i[2][0] == '+':
		cows[i[1]] += int(i[2][1:])
	else: cows[i[1]] -= int(i[2][1:])
	
	cur_max_num = max(cows.values())
	cur_max_cows = set()
	for j in cows.items(): 	
		if j[1] == cur_max_num: 
			cur_max_cows.add(j[0])
	if cur_max_cows != max_cows: 
		num_of_change += 1
		max_cows = cur_max_cows.copy()

print(num_of_change)
open('measurement.out', 'w').write(str(num_of_change))

