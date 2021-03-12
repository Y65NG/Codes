import hashlib
from multiprocessing import Pool

# def find(word, n):
# 	i = 1
# 	count = 0
# 	while True:
# 		binary = (word + str(i)).encode('utf-8')
# 		sha = hashlib.sha3_256(binary).hexdigest()
# 		if sha[:n] == '0' * n:
# 			print(sha)
# 			return count
# 		i += 1
# 		count += 1

def find(word, n):
	binary = (word + str(i)).encode('utf-8')
	sha = hashlib.sha3_256(binary).hexdigest()
	if sha[:n] == '0' * n:
		print(sha)
		return True
	return False

index = 0
while True:
	p = Pool(10)
	if p.apply_async(target = find, args = (index,)):
		print(index)
		break
	else: index += 1
print(find('An apple a day keeps doctor away', 7))

