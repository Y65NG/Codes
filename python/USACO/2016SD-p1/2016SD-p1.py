# return the total of numbers <= limit
def find(hays, limit):
	if limit < hays[0]: return 0
	high = len(hays)
	low = 0
	while high - low > 1:
		mid = (low + high) // 2
		#print(mid)
		if hays[mid] > limit: 
			high = mid
		else:
			low = mid
	#{print('low:', low)
	return low + 1
	
			
lines = open('haybales.in').read().strip().split('\n')
n, q = list(map(int, lines[0].split(' ')))
hays = list(map(int, lines[1].split(' ')))
queries = []
hays.sort()
for i in range(2, q + 2):
	queries.append(tuple(map(int, lines[i].split(' '))))

#print(hays)
file = open('haybales.out', 'w')
for i in range(q):
	r = queries[i]
	
	count = find(hays, r[1]) - find(hays, r[0] - 1)
	#print(r, find(hays, r[0]), find(hays, r[1]))
	print(count)
	file.write(str(count) + '\n')
file.close()
	

