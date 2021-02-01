def valid(mid):
	global n, letters
	visited = set()
	for i in range(n - mid + 1):
		if letters[i:i + mid] not in visited:
			visited.add(letters[i:i + mid])
		else: return False
	return True
	
lines = open('whereami.in').read().strip().split('\n')
n, letters = int(lines[0]), lines[1]

high = 100
low = 0
while high - low > 1:
	mid = (high + low) // 2
	if valid(mid): high = mid
	else: low = mid
print(high)

file = open('whereami.out', 'w')
file.write(str(high))
file.close()
