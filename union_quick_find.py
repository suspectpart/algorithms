class UnionFind(object):
	def __init__(self, n):
		self.nodes = [x for x in range(0, n)]
	def union(self, p, q):
		pid = self.nodes[p]
		qid = self.nodes[q]
		for index, item in enumerate(self.nodes):
			if item == pid:
				self.nodes[index] = qid
	def connected(self, p, q):
		return self.nodes[p] == self.nodes[q]