# 类
class ufds:
	# 建一个 n 个节点的 ufds
	def __init__(self, n):
		self.parents = list(range(n))

	# 寻找 u 的根结点
	def root(self, u):
		while self.parents[u] != u: u = self.parents[u]
		return u
	
	# 连接 u 和 v, O(logn)
	def union(self, u, v):
	    #if root(u) != root(v): parents[v] = u
	    if self.root(u) != self.root(v):
	        self.parents[self.root(v)] = self.root(u)
	
	# 判断 u 和 v 是否连在一起
	def find(self, u, v):
		return self.root(u) == self.root(v)
	
			
# 方法
parents = list(range(n))
def root(u): # O(logn)
    global parents
    while parents[u] != u: u = parents[u]
    return u

def union(u, v): # O(logn)
    global parents
    if root(u) != root(v):
        parents[root(v)] = root(u)

def find(u, v): # O(logn)
    return root(u) == root(v)
