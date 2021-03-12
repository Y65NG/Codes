import hashlib
from multiprocessing import Pool
import time

def find(word, n, start, end):
	for i in range(start, end):
		binary = (word + str(i)).encode('utf-8')
		sha = hashlib.sha3_256(binary).hexdigest()
		if sha[:n] == '0' * n:
			print(sha)
			return i - start
		

if __name__ == '__main__':
	index = 0
	p = Pool(10)
	n = int(1e3)
	r = range(0, 5 * 10 ** 7 + 1, n)
	
	start = time.time()
	for j in zip([x + 1 for x in r], r[1:]):
		# find('An apple a day keeps doctor away', 5, *j)
		p.apply_async(find, args = ('An apple a day keeps doctor away', 5, *j))
	# p.apply_async(find, args = ('An apple a day keeps doctor away', 5))
	
	p.close()
	p.join()
	end = time.time()
	print(end - start)
	# print(find('An apple a day keeps doctor away', 7))

