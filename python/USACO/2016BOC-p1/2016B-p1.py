def verify(a, b, k):
	return abs(a - b) <= k

lines = open('diamond.in', 'r').read().strip().split('\n')
header = list(map(int, lines[0].split(' ')))
n, k = header[0], header[1]
sizes = list(map(int, lines[1:]))
sizes.sort()

max_num = 0
for i in range(len(sizes) - 1):
	num = 0
	for j in range(i, len(sizes)):
		if verify(sizes[i], sizes[j], k): num += 1
	if num > max_num: max_num = num

print(max_num)
file = open('diamond.out', 'w')
file.write(str(max_num))
file.close()
