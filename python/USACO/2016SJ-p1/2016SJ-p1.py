lines = open('angry.in','r').read().strip().split('\n')

def valid(power):
	#print('power:', power)
	global N, K
	used = 0
	start = 0
	for used in range(K):
		for i in range(start, N):
			if power == 50: print(hay[start], hay[i])
			if hay[i] - hay[start] <= power:
				if i == N - 1:
					if power == 50: print('yes')
					return True
			else:
				#print(start, i)
				start = i
				break
	return False

data = lines[0].split(' ')
N, K = int(data[0]), int(data[1])
hay = []

for _ in range(1, N + 1):
	pos = int(lines[_])
	hay.append(pos)

high = 50000
low = 0
hay.sort()
#print(hay)
while high - low > 1:
	mid = (high + low) // 2
	#print(mid, high, low, valid(mid * 2))
	if not valid(mid * 2): low = mid
	else: high = mid
print(high)
f = open('angry.out', 'w')
f.write(str(high))
f.close

