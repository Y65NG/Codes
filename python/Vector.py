class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __add__(self, other):
		new = Vector(self.x + other.x, self.y + other.y)
		return new

	def __str__(self):
		return 'Vector({}, {})'.format(self.x, self.y)
		
	def __mul__(self, other):
		return self.x * other.x + self.y * other.y
	
v1 = Vector(3, 4)
v2 = Vector(2, 3)

print(v1 + v2, v1 * v2)

