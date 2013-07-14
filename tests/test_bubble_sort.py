from bubble_sort import sort
from nose.tools import *

def test_bubble_sort():
	items = [7,3,2,6,1,5,9,0,4]
	assert_equal(sort(items), sorted(items))
	assert_equal(sort(range(10)), sorted(range(10)))
	assert_equal(sort([]), [])