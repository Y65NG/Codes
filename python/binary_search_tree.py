class Node:
	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
	def search(self, data, parent):
		if self == None: return False, self, parent
		if self.data == data: return True, self, parent
		if self.data < data: return search(self.right, data, parent)
		else: return search(self.left, data, parent)
	
	def insert(self, data):
		if self == None: 
			self = Node(data)
			return
		if self.data < data: insert(self.right, data)
		else: insert(self.left, data)
	
	def delete(self, data, root):
		search(self, data, )
		
		
