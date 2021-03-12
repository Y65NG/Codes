import hashlib
from multiprocessing import Process, Pool
import time

def find(word, diff, start, end):
	for i in range(start, end):
		binary = (word + str(i)).encode('utf-8')
		sha = hashlib.sha3_256(binary).hexdigest()
		if sha[:diff] == '0' * diff:
			# print(sha)
			return i - start
		

if __name__ == '__main__':
	index = 0

	p = Pool(10)
	n = 10000
	r = range(0, 5 * 10 ** 11 + 1, n)
	
	start = time.time()
	for j in zip([x + 1 for x in r], r[1:]):
		# find('An apple a day keeps doctor away', 5, *j)
		p.apply_async(find, args = ('An apple a day keeps doctor away', 7, *j))
	# p.apply_async(find, args = ('An apple a day keeps doctor away', 5))
	
	
	end = time.time()
	print(end - start)
	# print(find('An apple a day keeps doctor away', 7))

