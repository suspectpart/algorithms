class UnionFind(object):
	def __init__(self,n):
		self.nodes = [x for x in range(0,n)]
		self.size = [1 for x in range(0,n)]
	def union(self, p, q):
		p_root = self.root(p)
		q_root = self.root(q)
		if self.size[p_root] < self.size[q_root]:
			self.subordinate(p_root, q_root)
		else:
			self.subordinate(q_root, p_root)
	def connected(self,p,q):
		return self.root(p) == self.root(q)
	def subordinate(self, smallRoot, bigRoot):
		self.nodes[smallRoot] = bigRoot
		self.size[bigRoot] += self.size[smallRoot]
	def root(self, x):
		if self.nodes[x] != x:
			return self.root(self.nodes[x])
		return x