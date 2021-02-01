def valid(count):
	if count >= b: return True
	for i in range(len(intervals) - count):
		
		if sum(intervals[i:i + count + 1]) + count >= k:
			print(sum(intervals[i:i + count + 1]) + count)
			return True
	print(sum(intervals[i:i + count + 1]) + count)
	return False



lines = open('maxcross.in').read().strip().split('\n')
data = list(map(int, lines[0].split(' ')))
n, k, b = data
brokens = [] 
intervals = []
for i in range(1, b + 1):
	brokens.append(int(lines[i]))

brokens.sort()

for i in range(len(brokens) - 1):
	intervals.append(brokens[i + 1] - brokens[i] - 1)
#print(intervals)

file = open('maxcross.out', 'w')
if len(intervals) == 0: 
	file.write('0')
	file.close()

else:
	
	low = -1
	high = 100000
	while high - low > 1:
		mid = (low + high) // 2
		judge = valid(mid)
		print(mid, judge)
		if judge: high = mid
		else: low = mid
	
	print(high)
	
	file.write(str(high))
	file.close()
		
		
