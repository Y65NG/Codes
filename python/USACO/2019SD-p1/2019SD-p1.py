n = int(open('moobuzz.in').read().strip())
grid = (n - 1) // 8
remain = (n - 1) % 8
num = grid * 15 + 1
index = -1

while index < remain:
	if num % 3 != 0 and num % 5 != 0:
		index += 1
	num += 1
	
print(num - 1)
file = open('moobuzz.out', 'w')
file.write(str(num - 1))
file.close()
