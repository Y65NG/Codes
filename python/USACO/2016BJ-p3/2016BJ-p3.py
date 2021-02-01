lines = open('mowing.in', 'r').read().strip().split('\n')

def overlap(pos):
	try:
		visited[pos]
		return True
	except:
		return False

def move(dir, step):
	global t, visited, pos, min_interval
	if dir == 'N':
		for i in range(step):
			if not overlap((pos[0], pos[1] + i)):
				visited[(pos[0], pos[1] + i)] = t
				
			else:
				#print(pos, i,t)
				interval = t - visited[(pos[0], pos[1] + i)]
				if interval < min_interval: min_interval = interval
				visited[(pos[0], pos[1] + i)] = t
			t += 1
		pos = (pos[0], pos[1] + step)
	elif dir == 'S':
		for i in range(step):
			
			if not overlap((pos[0], pos[1] - i)):
				visited[(pos[0], pos[1] - i)] = t
				
			else:
				#print(pos,i,t)
				interval = t - visited[(pos[0], pos[1] - i)]
				if interval < min_interval: min_interval = interval
				visited[(pos[0], pos[1] - i)] = t
			t += 1
		pos = (pos[0], pos[1] - step)
		
	elif dir == 'W':
		for i in range(step):
			
			if not overlap((pos[0] - i, pos[1])):
				visited[(pos[0] - i, pos[1])] = t
				
			else:
				#print(pos,i,t)
				interval = t - visited[(pos[0] - i, pos[1])]
				if interval < min_interval: min_interval = interval
				visited[(pos[0] - i, pos[1])] = t
			t += 1
		pos = (pos[0] - step, pos[1])
	elif dir == 'E':
		for i in range(step):
			
			if not overlap((pos[0] + i, pos[1])):
				visited[(pos[0] + i, pos[1])] = t
				
			else:
				
				interval = t - visited[(pos[0] + i, pos[1])]
				if interval < min_interval: min_interval = interval
				visited[(pos[0] + i, pos[1])] = t
			t += 1
		pos = (pos[0] + step, pos[1])
		
def processing():
	global N, pos, visited, t, min_interval
	for i in range(N):
		move(steps[i][0], steps[i][1])
		#print(min_interval)
	

N = int(lines[0])
visited = {}
pos = (0, 0)
t = 0
steps = []
min_interval = float('inf')
for _ in range(1, N + 1):
	line = lines[_].split(' ')
	dir = line[0]
	step = int(line[1])
	steps.append((dir, step))
#print(steps)

processing()
if min_interval == float('inf'): min_interval = -1
#print(visited)
print(min_interval)
file = open('mowing.out', 'w')
file.write(str(min_interval))
file.close()




