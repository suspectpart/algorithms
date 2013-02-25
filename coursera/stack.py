class Stack(object):
	'''the most unnecessary class ever written'''
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		if self.count() == 0:
			return None
		return self.items.pop()
	def count(self):
		return len(self.items)