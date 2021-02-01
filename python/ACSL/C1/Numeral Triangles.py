s, d, r = input().split(' ')
r = int(r)

nums = []

def sumDigits(hexNum):
	total = 0
	for i in hexNum:
		total += int(i, 16)
	return total

def sumOfLastRow(s, d, r):
	delta = int(d, 16)
	row = 1
	nums.append(s)
	while row <= r:
		for i in range(row): nums.append(hex(int(nums[-1], 16) + delta)[2:])
		row += 1
	result = nums[-r - 1: -1]
	#print(result)
	total = 0
	for num in result:
		total += sumDigits(num)
	total = hex(total)[2:]
	
	while len(total) > 1:
		total = hex(sumDigits(total))[2:]
	return total.upper()
	
print(sumOfLastRow(s, d, r))
