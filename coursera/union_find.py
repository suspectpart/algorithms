class UnionFind(object):
	def __init__(self, items):
		self._items_ = items
		self._components_ = [[x] for x in range(0,self._items_)]
	def union(self, p,q):
		if(p > self._items_ or q > self._items_):
			print "can not connect {0} and {1}".format(p,q)
			return
			
		joinedComponent = []
		for component in self._components_:
			if(component.count(p) > 0 or component.count(q) > 0):
				joinedComponent.extend(component)
				self._components_.remove(component)
		
		joinedComponent.extend([p,q])
		self._components_.append(list(set(joinedComponent)))
		
		print 'connected {0} and {1}'.format(p,q)
	def connected(self, p,q):
		found = False;
		
		for component in self._components_:
			found = (component.count(p) + component.count(q)) == 2
			
		print found
	
	
u = UnionFind(10)
u.union(1,2)
u.union(3,4)
u.union(4,5)
u.union(5,6)
u.union(5,11)
u.union(11,5)
u.connected(1,6)
u.connected(2,6)
u.connected(3,4)
u.connected(3,5)
u.connected(3,6)
u.connected(6,6)
u.connected(6,11)
