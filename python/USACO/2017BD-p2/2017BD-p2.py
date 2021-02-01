lines = open('shuffle.in', 'r').read().strip().split('\n')
n = int(lines[0])
cows = [0] * (n + 1)
shuffle = [0] + list(map(int, lines[1].split(' ')))
final_pos = [0] + list(map(int, lines[2].split(' ')))
for _ in range(3):
	
	for i in range(1, n + 1):
		cows[i] = final_pos[shuffle[i]]
		
	final_pos = cows[:]
	#print(final_pos)

file = open('shuffle.out', 'w')
for i in range(1, len(cows)): 
	print(cows[i])
	file.write(str(cows[i]) + '\n')
file.close()
