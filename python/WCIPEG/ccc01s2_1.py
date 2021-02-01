def move(num, pos, dir, step):
	global result, end
	x, y = pos[0], pos[1]
	for i in range(1, step + 1): 
		if num + i <= end: 
			if dir == 0: 
				result[x + i][y] = num + i
				pos[0] += 1
			elif dir == 1: 
				result[x][y + i] = num + i
				pos[1] += 1
			elif dir == 2: 
				result[x - i][y] = num + i
				pos[0] -= 1
			else: 
				result[x][y - i] = num + i
				pos[1] -= 1
		else:
			if dir == 0: 
				result[x + i][y] = -1
				pos[0] += 1
			elif dir == 1: 
				result[x][y + i] = -1
				pos[1] += 1
			elif dir == 2: 
				result[x - i][y] = -1
				pos[0] -= 1
			else: 
				result[x][y - i] = -1
				pos[1] -= 1
	
	return num + step
	
def change_dir(dir):
	if dir < 3: return dir + 1
	return 0

def process(start, end):
	global result
	pos = [50, 50]
	num = start
	dir = 0
	step = 1
	while num < end:
		for i in range(2):
			if num > end: break
			#print(dir, step, end = ',')
			num = move(num, pos, dir, step)
			#print(num)
			dir = change_dir(dir)
		step += 1

def print_result(result):
	string = ''
	for i in range(100):
		judge = False
		for j in range(100):
			if result[i][j] < 0:
				judge = True
				string += '  '
			elif result[i][j] > 0:
				judge = True
				string += str(result[i][j]) + ' '
		if judge: string += '\n'
	print(string)


start = int(input())
end = int(input())
result = [[0] * 100 for i in range(100)]
result[50][50] = start
process(start, end)
print_result(result)
#print(result[50][47:55])
