import math

class Vector(object):
	def __init__(self, a, b, c):
		self.coords = (a,b,c)

	def scalar_product(self, other):
		return sum([x * y for x, y in zip(self.coords, other.coords)])

	def orthogonal_to(self, other):
		return self.scalar_product(other) == 0

	def add(self, other):
		a1, b1, c1 = self.coords
		a2, b2, c2 = other.coords
		return Vector(a1 + a2, b1 + b2, c1 + c2)

	def subtract(self, other):
		a1, b1, c1 = self.coords
		a2, b2, c2 = other.coords
		return Vector(a1 - a2, b1 - b2, c1 - c2)

	def magnitude(self):
		return math.sqrt(sum([x**2 for x in self.coords]))

	'''
	The angle is defined as a * b = |a| * |b| * cos(alpha),
	so we can say 
	    cos(alpha) = a * b / |a| * |b|
	<-> alpha = acos(a * b / |a| * |b|)
	'''
	def angle(self, other):
		return math.degrees(math.acos(self.scalar_product(other) / (self.magnitude() * other.magnitude())))

	def parallel_to(self, other):
		a1, b1, c1 = self.coords
		a2, b2, c2 = other.coords
		return a2 / a1 == b2 / b1 == c2 / c1