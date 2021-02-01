pails = list(map(int, open('pails.in', 'r').read().strip().split(' ')))
X, Y, M = pails[0], pails[1], pails[2]
max_Y = 0
max_pail = 0
while Y * max_Y <= M:
	max_Y += 1
max_Y -= 1

for i in range(max_Y, -1, -1):
	max_X = 0
	while X * max_X + Y * i <= M:
		max_X += 1
	max_X -= 1
	if X * max_X + Y * i > max_pail: max_pail = X * max_X + Y * i
print(max_pail)
file = open('pails.out', 'w')
file.write(str(max_pail))
file.close()
