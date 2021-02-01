lines = open('helpcross.in').read().strip().split('\n')
data = list(map(int, lines[0].split(' ')))
c, n = data[0], data[1]
prefix = [0] * 1000000 # prefix with each grid of size 1000
chickens = []
cows = []
count = 0
for i in range(1, c + 1):
	chickens.append(int(lines[i]))
for i in range(c + 1, n + c + 1):
	cows.append(tuple(map(int, lines[i].split(' '))))

chickens.sort()
for i in range(1, len(chickens)):
	prefix[chickens[i] // 1000] += 1 + prefix[chickens[i] // 1000 - 1]
#print(chickens, cows)
#print(prefix[0:3])

