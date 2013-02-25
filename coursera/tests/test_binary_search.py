from nose.tools import *
from binary_search import BinarySearch

def test_binary_search():
	numbers = [0,3,5,12,17,23,34,78,134]
	sut = BinarySearch(numbers)
	eq_(sut.search(0), 0)
	eq_(sut.search(3), 1)
	eq_(sut.search(17), 4)
	eq_(sut.search(134), 8)
	eq_(sut.search(135), -1)
	