class UnionFind(object):
	def __init__(self,n):
		self._nodes_ = [x for x in range(0,n)]
	def union(self, p, q):
		self._nodes_[self.root(p)] = self.root(q)
	def connected(self,p,q):
		return self.root(p) == self.root(q)
	def root(self, x):
		if(x != self._nodes_[x]):
			return self.root(self._nodes_[x])
		return x