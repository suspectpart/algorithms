import unittest

# One way to write unittests
class TestUnionFindFixture(unittest.TestCase):
	def test_union_find(self): 
		"""This is a docstring (like a ///<summary comment in c#>)"""
		self.assertEqual(1, 0)

	def test_some_other_stuff(self):	
		"""Only methods that are prefixed with test will be run"""
		self.assertEqual(1, 1)

# This is an idiomatic main function. This is usefull because any python file could be included as a module. 
# This decides what should happen when you call this script directly. 
# This is actually not the ideal way of calling this test...
if __name__ == '__main__':
	unittest.main() # Obviously, this runns your tests.