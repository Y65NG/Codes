from functools import total_ordering

def reversed(str):
		result = ''
		for i in range(len(str) - 1, -1, -1):
			result += str[i]
		return result

def larger(n1, n2):
	if len(n1) > len(n2): return True
	elif len(n1) < len(n2): return False
	else: 
		for i in range(len(n1)):
			d1, d2 = int(n1[i]), int(n2[i])
			if d1 > d2: return True
			else: return False

class Big_integer:
	
	def __init__(self, num, neg):
			self.neg = neg
			self.num = num
		
	
	def __len__(self):
		return len(self.num)
	
	def __str__(self):
		return self.num
		
	def __eq__(self, other):
		return self.num == other.num
		
	def __lt__(self, other):
		n1 = self.num
		n2 = other.num
		if self.neg:
			if other.neg:
				return larger(n1, n2)
			else: return True
		else: 
			if other.neg:
				return False
			else: return not larger(n1, n2)
	
	def __add__(self, other):
		result = ''
		max_length = max(len(self.num), len(other.num))
		#print(max_length)
		if len(self.num) < max_length: self.num = '0' * (max_length - len(self.num)) + self.num
		elif len(other.num) < max_length: other.num = '0' * (max_length - len(other.num)) + other.num
		#print(self.num, other.num)
		carry = 0
		for i in range(max_length - 1, -1, -1):
			d1, d2 = int(self.num[i]), int(other.num[i])
			sum = d1 + d2
			if carry != 0:
				sum += carry
				carry = 0
			if sum >= 10:
				carry = sum // 10
				sum = sum % 10
			result += str(sum)
		if carry != 0:
			result += str(carry)

		return Big_integer(reversed(result))
		
	def __sub__(self, other):
		result = ''
		neg = False
		if self.num < other.num: neg = True
		
		max_length = max(len(self.num), len(other.num))
		#print(max_length)
		if len(self.num) < max_length: self.num = '0' * (max_length - len(self.num)) + self.num
		elif len(other.num) < max_length: other.num = '0' * (max_length - len(other.num)) + other.num
		#print(self.num, other.num)
		
		carry = 0
		for i in range(max_length - 1, -1, -1):
			d1, d2 = int(self.num[i]), int(other.num[i])
			if d1 - d2 < 0:
				d1 += 10
				carry = 1
			diff = d1 - d2
			if carry != 0:
				diff -= carry
				carry = 0
			if diff <= 10:
				carry = sum // 10
				sum = sum % 10
			result += str(sum)
		if carry != 0:
			result += str(carry)

		return Big_integer(reversed(result))
