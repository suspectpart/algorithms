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
		
		
union = UnionFind(3)
print union.connected(0,1) == False
print union.connected(1,2) == False
union.union(0,1) #[0,1,2] -> [1,1,2]
print union.connected(0,1)
print union.connected(1,2) == False
union.union(1,2) #[1,1,2] -> [2,2,2] 
print union.connected(2,0)