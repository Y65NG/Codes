def neighbors(hay, radius):
	global exploded
	
	result = set()
	for i in range(hay + 1, len(hays)):
		if hays[i] > hays[hay] + radius: break
		if i not in exploded: result.add(i)
		
	for i in range(hay - 1, -1, -1):
		if hays[i] < hays[hay] - radius: break
		if i not in exploded: result.add(i)
	
	return result

def explode(hay, radius):
	global hays, exploded
	
	r = radius + 1
	if len(neighbors(hay, r)) == 0: return 1
	for i in neighbors(hay, r):
		exploded.add(i)
		explode(i, r)
		
		
	

lines = open('1.in', 'r').read().strip().split('\n')
N = int(lines[0])
hays = []

max_hay = 0

for _ in range(1, N + 1):
	hay = int(lines[_])
	hays.append(hay)

hays.sort()
print(hays)
for i in range(len(hays)):
	exploded = {i}
	explode(i, 0)
	print(i,exploded)
	if len(exploded) > max_hay: 
		#print(num)
		max_hay = len(exploded)
		print('index:', i)
		#print(max_hay, max_index)
print('max:', max_hay)
file = open('1.out', 'w')
#file.write(str(max_hay))
file.close()




