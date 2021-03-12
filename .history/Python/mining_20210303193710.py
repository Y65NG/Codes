import hashlib

def find(word, n):
	i = 1
	count = 0
	while True:
		binary = (word + str(i)).encode('utf-8')
		sha = hashlib.sha3_256(binary).hexdigest()
		if sha[:n] == '0' * n:
			print(sha)
			return(count)
		i += 1
		count += 1
print(find('An apple a day keeps doctor away', 7))

