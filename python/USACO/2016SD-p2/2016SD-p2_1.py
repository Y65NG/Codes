lines = open('citystate.in').read().strip().split('\n')
n = int(lines[0])
pairs = {}
for i in lines[1:]:
	pair = i.split(' ')
	string = pair[0][:2] + pair[1]
	if string[:2] != string[2:]:
		if string not in pairs: pairs[string] = 1
		else: pairs[string] += 1

count = 0
for string in pairs:
	rev = string[2:] + string[:2]
	print(string, rev)
	if rev in pairs:
		print('yes')
		count += pairs[string] * pairs[rev]
print(count // 2)
file = open('citystate.out', 'w')
file.write(str(count // 2))
