#
class UnionFind(object):
	def __init__(self, n):
		self._nodes_ = [x for x in range(0, n)]
	def union(self, p, q):
		pid = self._nodes_[p]
		qid = self._nodes_[q]
		for index, item in enumerate(self._nodes_):
			if(item == pid):
				self._nodes_[index] = qid
	def connected(self, p, q):
		return self._nodes_[p] == self._nodes_[q]