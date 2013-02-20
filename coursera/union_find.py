class UnionFind(object):
	def __init__(self, items):
		self.items = items
		self.components = [[x] for x in range(0,self.items)]
	def union(self, p,q):
		joinedComponent = []
		for component in self.components:
			if component.count(p) > 0 or component.count(q) > 0:
				joinedComponent.extend(component)
				self.components.remove(component)
		
		joinedComponent.extend([p,q])
		self.components.append(list(set(joinedComponent)))
	def connected(self, p,q):
		found = False;
		
		for component in self.components:
			found = (component.count(p) + component.count(q)) == 2
			
		return found