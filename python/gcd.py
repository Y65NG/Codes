def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)
	
def lcm(a, b):
	return a * b // gcd(a, b)
	
def exgcd(a, b):
	global x, y
	
	if b == 0:
		x = 1
		y = 0
		return a
	g = exgcd(b, a % b, x, y)
	temp = x
	x = y
	y = temp - a // b * y
	return g
