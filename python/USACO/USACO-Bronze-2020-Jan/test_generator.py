import random
n = random.randint(1, 50)
result = str(n) + '\n'
for i in range(n):
	if random.randint(0, 1) == 0: dir = 'N '
	else: dir = 'E '
	x, y = random.randint(0, 100), random.randint(0, 100)
	result += dir + str(x) + ' ' + str(y) + '\n'
print(result)
file = open('test3ran.txt', 'w')
file.write(result)
file.close()
