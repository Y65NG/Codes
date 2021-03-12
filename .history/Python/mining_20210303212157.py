import hashlib
from multiprocessing import Pool

def find(word, n):
	i = 1
	count = 0
	while True:
		binary = (word + str(i)).encode('utf-8')
		sha = hashlib.sha3_256(binary).hexdigest()
		if sha[:n] == '0' * n:
			print(sha)
			return count
		i += 1
		count += 1

# def find(word, n):
# 	binary = (word + str(n)).encode('utf-8')
# 	sha = hashlib.sha3_256(binary).hexdigest()
# 	if sha[:n] == '0' * n:
# 		print(sha)
# 		return True
# 	return False
if __name__ == '__main__':
	index = 0
	p = Pool(10)
	# result = p.map(find, ('An apple a day keeps doctor away', 4, ))
	# print(result)
	p.apply_async(find, args = ('An apple a day keeps doctor away', 7))
	# for i in range(100000000000000):
	# 	if p.apply_async(find, args = ('An apple a day keeps doctor away', index,)):

	# 		print(index)
	# 		break
		# else: index += 1
	p.close()
	p.join()
	# print(find('An apple a day keeps doctor away', 7))

