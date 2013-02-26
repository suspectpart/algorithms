from stack import Stack
import re

class Djikstra(object):
	def __init__(self):
		self.values = Stack()
		self.operators = Stack()

	def parse(self, expression):
		self.values.push(0)
		for char in expression:
			if char.isdigit():
				self.values.push(float(char))
			elif self.is_operator(char):
				self.operators.push(char)
			elif char == ')':
				x = self.values.pop()
				y = self.values.pop()
				op = self.operators.pop()
				result = self.apply_operator_to(op,x,y)
				self.values.push(result)
		return self.values.pop()
	
	def is_operator(self, char):
		return char in "+*-/"
	
	def apply_operator_to(self,op,x,y):
		if op in "/-":
			x,y = y,x
		return eval("{0}{1}{2}".format(x,op,y))
