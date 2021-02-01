nums = list(map(int, open('div7.in', 'r').read().strip().split('\n')))
prev = [nums[0]]
remainders = {}
max_length = 0

for i in range(1, len(nums)):
	prev.append(prev[i - 1] + nums[i])

for i in range(len(prev)):
	try: 
		index = remainders[prev[i] % 7]
		if i - index > max_length: max_length = i - index
	except:
		remainders[prev[i] % 7] = i
print(max_length)
file = open('div7.out', 'w')
file.write(str(max_length))
file.close()
		




