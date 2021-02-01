n = int(input())
petals = list(map(int, input().split(' ')))
total_photo = n
for r in range(2, n + 1):
	for i in range(n - r + 1):
		total = sum(petals[i:i + r])
		if total % r != 0: continue
		else:
			avg = total // r
			if avg in petals[i:i + r]: 
				total_photo += 1
				
print(total_photo)
