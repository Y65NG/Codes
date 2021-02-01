def win(a, b, i):
	global gestures, prefix

	count = 0
	
	count += prefix[i][a] + prefix[-1][b] - prefix[i][b]
	return count

lines = open('hps.in').read().strip().split('\n')
n = int(lines[0])
gestures = lines[1:]
prefix = []
for i in range(n):
	if i == 0:
		if gestures[i] == 'H': prefix.append((1,0,0))
		elif gestures[i] == 'P': prefix.append((0, 1, 0))
		else: prefix.append((0,0,1))
	else:
		h = prefix[i - 1][0]
		p = prefix[i - 1][1]
		s = prefix[i - 1][2]
		if gestures[i] == 'H': prefix.append((h + 1, p, s))
		elif gestures[i] == 'P': prefix.append((h, p + 1, s))
		else: prefix.append((h, p, s + 1))
# print(gestures, prefix)

max_count = 0
for i in range(n):
	count = max(win(0, 1, i), win(0, 2, i), win(1, 0, i), win(1, 2, i), win(2, 0, i), win(2, 1, i))
	max_count = max(max_count, count)
	
print(max_count)
file = open('hps.out', 'w')
file.write(str(max_count))
file.close()
