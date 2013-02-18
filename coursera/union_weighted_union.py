class UnionFind(object):
	def __init__(self,n):
		self._nodes_ = [x for x in range(0,n)]
		self._size_ = [1 for x in range(0,n)]
	def union(self, p, q):
		p_root = self.root(p)
		q_root = self.root(q)
		if(self._size_[p_root] < self._size_[q_root]):
			self._nodes_[p_root] = q_root
			self._size_[q_root] += self._size_[p_root]
		else:
			self._nodes_[self.root(q)] = self.root(p)
			self._size_[p_root] += self._size_[q_root]
	def connected(self,p,q):
		return self.root(p) == self.root(q)
	def root(self, x):
		if(x != self._nodes_[x]):
			return self.root(self._nodes_[x])
		return x