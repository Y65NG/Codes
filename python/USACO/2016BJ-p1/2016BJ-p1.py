lines = open('promote.in', 'r').read().strip().split('\n')
before = []
after = []
promoted = [0] * 3
for _ in range(len(lines)):
	data = list(map(int, lines[_].split(' ')))
	before.append(data[0]) 
	after.append(data[1])
new_people = sum(after) - sum(before)

promoted[2] = after[3] - before[3]
promoted[1] = after[2] - before[2] + promoted[2]
promoted[0] = after[1] - before[1] + promoted[1]
file = open('promote.out', 'w')
for i in promoted: 
	print(i)
	file.write(str(i) + '\n')
file.close()

	
