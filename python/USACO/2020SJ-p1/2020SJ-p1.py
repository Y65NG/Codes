def valid(mid):
	global N, K, trees

	

lines = open('berries.in').read().strip().split('\n')
N, K = [int(x) for x in lines[0].split(' ')]
trees = [int(x) for x in lines[1].split(' ')]
trees.sort()

high = 1000000
low = 0
while high - low > 1:
	mid = (high + low) // 2
	if valid(mid): high = mid
	else: low = mid

print(mid)