def distance(index):
	global capacities, total
	dis = 0
	pos = index + 1
	if pos == len(capacities): pos = 0
	remain = total
	while pos != index:
		remain -= capacities[pos]
		dis += remain
		
		if pos != len(capacities) - 1: pos += 1
		else: pos = 0
	return dis
	
lines = list(map(int, open('cbarn.in', 'r').read().strip().split('\n')))
n = lines[0]
capacities = lines[1:]
min_distance = float('inf')
total = sum(capacities)

for index in range(len(capacities)):
	#print(distance(index))
	if distance(index) < min_distance: min_distance = distance(index)

print(min_distance)
file = open('cbarn.out', 'w')
file.write(str(min_distance))
file.close()
