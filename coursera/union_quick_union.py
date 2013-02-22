class UnionFind(object):
	def __init__(self,n):
		self.nodes = range(n)
	def union(self, p, q):
		self.nodes[self.root(p)] = self.root(q)
	def connected(self,p,q):
		return self.root(p) == self.root(q)
	def root(self, x):
		if x != self.nodes[x]:
			return self.root(self.nodes[x])
		return x