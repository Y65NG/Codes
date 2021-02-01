import random
def generate_prime(n):
	nums = [True] * (n + 1)
	for i in range(2, int(n ** 0.5) + 1):
		if nums[i]:
			for j in range(2 * i, n + 1, i):
				nums[j] = False
	result = []
	for i in range(2, len(nums)):
		if nums[i]: result.append(i)
	index = random.randint(0, len(result) - 1)
	print(result)

while True:
	generate_prime(int(input()))
