from nose.tools import *
# This is a test written with nose tests.
# I like it better, because it does not have the overhead of a class
# and provides nicer test functions that can be called without the 
# explicit self parameter! 

# Run this test by executing 
# $ nosetests
# from your root folder 
def test_union_find(): 
	"""If you run nose with --verbose the docstring will be shown!"""
	assert_equal(1, 0) 

def test_some_other_stuff():	
	assert_equal(1, 1) # Nose comes with more readable assertion functions