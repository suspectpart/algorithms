class Queue(object):
	"""
	Queue implementation with a linked list. 
	Takes constant time with every operation but consumes more memory than an array resize approach
	"""
	
	def __init__(self):
		self.first = None
		self.last = None
	def enqueue(self, value):
		previous_last = self.last
		self.last = Node(value, next = None)
		if not self.is_empty():
			previous_last.next = self.last
		else:
			self.first = self.last
	def dequeue(self):
		if self.is_empty():
			return None
		item = self.first
		self.first = self.first.next
		return item.cargo
	def is_empty(self):
		return self.first == None

class Node(object):
	def __init__(self, cargo, next):
		self.next = next
		self.cargo = cargo