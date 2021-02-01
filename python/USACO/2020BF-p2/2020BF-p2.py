def change(text, start, end):
	result = ''
	for i in range(start, end):
		if text[i] == 'H': result += 'G'
		else: result += 'H'
	return text[:start] + result + text[end:]

lines = open('breedflip.in').read().strip().split('\n')
N = int(lines[0])
A, B = lines[1:]

count = 0
index = 0
while index < N:
	if A[index] != B[index]:
		i = index + 1
		while i < N:
			if A[i] == B[i]: break
			i += 1
		change(B, index, i)
		count += 1
		index = i
	else: index += 1

print(count)
file = open('breedflip.out', 'w')
file.write(str(count))
file.close()
