from nose.tools import *
from vectors import Vector
import math

def test_init():
	eq_(Vector(1,2,3).coords, (1,2,3))

def test_scalar_product():
	v1 = Vector(1,2,3)
	v2 = Vector(4,5,6)
	scalar_product = v1.scalar_product(v2)
	eq_(scalar_product, 1*4 + 2*5 + 3*6)

def test_vectors_orthogonal():
	v1 = Vector(1,2,1)
	v2 = Vector(-1,2,-3)
	v3 = Vector(2,1,2)
	eq_(v1.orthogonal_to(v2), True)
	eq_(v1.orthogonal_to(v3), False)

def test_add_vectors():
	v1 = Vector(1,2,3)
	v2 = Vector(4,5,6)
	v3 = v1.add(v2)
	eq_(v3.coords, (1+4, 2+5, 6+3))

def test_subtract_vectors():
	v1 = Vector(1,2,3)
	v2 = Vector(4,5,6)
	v3 = v1.subtract(v2)
	eq_(v3.coords, (1-4, 2-5, 3-6))

def test_magnitude():
	vector = Vector(1,2,3)
	magnitude = math.sqrt(1**2 + 2**2 + 3**2)
	eq_(vector.magnitude(), magnitude)

def test_angle():
	v1 = Vector(1,2,3)
	v2 = Vector(4,5,6)
	angle = math.degrees(math.acos(v1.scalar_product(v2) / (v1.magnitude() * v2.magnitude())))
	eq_(v1.angle(v2), angle)

def test_parallel():
	v1 = Vector(1,2,3)
	v2 = Vector(3,6,9)
	v3 = Vector(3,2,1)
	eq_(v1.parallel_to(v2), True)
	eq_(v1.parallel_to(v3), False)

def test_equals():
	v1 = Vector(1,2,3)
	v2 = Vector(1,2,3)
	eq_(v1.equals(v2), True)