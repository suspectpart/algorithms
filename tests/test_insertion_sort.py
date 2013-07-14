from nose.tools import *
from insertion_sort import InsertionSort

def test_insertion_sort():
	sort = InsertionSort() 
	unsorted_numbers = [9,3,5,1,4,5,7]
	assert_equals(sort.sort(unsorted_numbers), sorted(unsorted_numbers))