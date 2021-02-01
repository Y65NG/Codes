lines = open('taming.in').read().strip().split('\n')
n = int(lines[0])
days = list(map(int, lines[1].split(' ')))
days[0] = 0
temp = days.copy()
judge = False

index = n - 1
while index > 0:
	if judge: break
	num = days[index]
	if num == -1: index -= 1
	else:
		for i in range(1, num + 1):
			if days[index - i] == -1: temp[index - i] = num - i
			elif days[index - i] == num - i: continue
			else: 
				judge = True
				break
		index -= num + 1
print(days, temp)

file = open('taming.out', 'w')
if judge:
	print(-1)
	file.write('-1')
else:
	count_num = 0
	count_unknown = 0
	for i in temp:
		if i == 0: count_num += 1
		elif i == -1: count_unknown += 1
	print(count_num, count_num + count_unknown)
	
	file.write(str(count_num) + ' ' + str(count_num + count_unknown))
