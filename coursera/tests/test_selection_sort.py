from nose.tools import *
from selection_sort import SelectionSort

def test_selection_sort():
	sort = SelectionSort()
	unsorted_numbers = [9,3,5,1,4,5,7]
	assert_equals(sort.these(unsorted_numbers), sorted(unsorted_numbers))