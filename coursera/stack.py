class Stack(object):
	'''the most unnecessary class ever written'''
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		if self.is_empty():
			return None
		return self.items.pop()
	def is_empty(self):
		return self.count() == 0
	def count(self):
		return len(self.items)