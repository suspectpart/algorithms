class UnionFind(object):
	def __init__(self, items):
		self._items_ = items
		self._components_ = [[x] for x in range(0,self._items_)]
	def union(self, p,q):
		joinedComponent = []
		for component in self._components_:
			if(component.count(p) > 0 or component.count(q) > 0):
				joinedComponent.extend(component)
				self._components_.remove(component)
		
		joinedComponent.extend([p,q])
		self._components_.append(list(set(joinedComponent)))
	def connected(self, p,q):
		found = False;
		
		for component in self._components_:
			found = (component.count(p) + component.count(q)) == 2
			
		return found