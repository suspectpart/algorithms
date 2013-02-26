from nose.tools import *
from djikstra_algorithm import Djikstra

def test_empty_string():
	djikstra = Djikstra()
	eq_(djikstra.parse(""), 0)
	
def two_values_and_the_same_operator():
	djikstra = Djikstra()
	eq_(djikstra.parse("(0+0)"), 0)
	eq_(djikstra.parse("(0*0)"), 0)
	eq_(djikstra.parse("(1+1)"), 1)
	eq_(djikstra.parse("(1*1)"), 1)
	eq_(djikstra.parse("(9+9)"), 18)
	eq_(djikstra.parse("(9*9)"), 81)
	
def test_more_values_and_the_same_operator():
	djikstra = Djikstra()
	eq_(djikstra.parse("(3+(3+3))"), 9)
	eq_(djikstra.parse("(3+((3+3)+(3+3)))"), 3 * 5)
	eq_(djikstra.parse("(3*(3*3))"), 27)
	eq_(djikstra.parse("(3*((3*3)*(3*3)))"), 3 ** 5)

def test_more_values_and_different_operators():
	djikstra = Djikstra()
	eq_(djikstra.parse("(3+(3*3))"), 12)
	eq_(djikstra.parse("(3+((3*3)+(3*3)))"), 21)
