class Stack(object):
	'''
	the most unnecessary class ever written, as python lists somehow are stacks already.
	using a list to store the items follows the array resize approach, where pushing items
	in most cases takes constant time with some peeks to resize / shrink (?) the list 
	(i am not sure if python shrinks lists when you remove items. 
	The .NET Stack impementation doesn't, for example. 
	Another approach would be to use a linked list,
	which consumes more memory but always takes constant time to push and pop
	'''
	def __init__(self):
		self.clear()
	def push(self, item):
		self.items.append(item)
	def peek(self):
		if self.is_empty():
			return None
		return self.items[-1]
	def pop(self):
		if self.is_empty():
			return None
		return self.items.pop()
	def is_empty(self):
		return self.count() == 0
	def count(self):
		return len(self.items)
	def clear(self):
		self.items = []