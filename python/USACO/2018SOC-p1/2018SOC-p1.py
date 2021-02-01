lines = open('sort.in').read().strip().split('\n')
N, arr = int(lines[0]), [int(x) for x in lines[1:]]

count = 0
sorted = False
#print(N, arr)
while not sorted:
	sorted = True
	count += 1
	for i in range(0, N - 1):
		if arr[i + 1] < arr[i]:
			arr[i], arr[i + 1] = arr[i + 1], arr[i]
			sorted = False

#print(arr)

print(count)
file = open('sort.out', 'w')
file.write(str(count))
file.close()
