lines = open('haybales.in').read().strip().split('\n')
n, q = list(map(int, lines[0].split(' ')))
data = list(map(int, lines[1].split(' ')))
queries = []
for i in range(2, q + 2):
	queries.append(tuple(map(int, lines[i].split(' '))))

hays = [0] * 1000000000
pre = [0] * 1000000
for i in data:
	hays[i] = 1

pre[0] = hays[0]
for i in range(1, 10001):
	pre[i] = pre[i - 1] + hays[i]
	
print(pre[2:8])
file = open('haybales.out', 'w')
for i in range(q):
	r = queries[i]
	count = pre[r[1]] - pre[r[0] - 1]

	print(count)
	file.write(str(count) + '\n')
file.close()

