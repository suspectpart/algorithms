from nose.tools import *
from djikstra_algorithm import Djikstra

def test_empty_string():
	djikstra = Djikstra()
	eq_(djikstra.parse(""), 0)
	
def test_two_values_and_the_same_operator():
	djikstra = Djikstra()
	eq_(djikstra.parse("(0+0)"), 0)
	eq_(djikstra.parse("(0*0)"), 0)
	eq_(djikstra.parse("(1+1)"), 2)
	eq_(djikstra.parse("(1*1)"), 1)
	eq_(djikstra.parse("(9+9)"), 18)
	eq_(djikstra.parse("(9*9)"), 81)
	eq_(djikstra.parse("(4-3)"), 1)
	eq_(djikstra.parse("(8/4)"), 2)
	
def test_more_values_and_the_same_operator():
	djikstra = Djikstra()
	eq_(djikstra.parse("(3+(3+3))"), 9)
	eq_(djikstra.parse("(3*(3*3))"), 27)
	eq_(djikstra.parse("(9-(4-3))"), 8)
	eq_(djikstra.parse("(8/(4/2))"), 4)
	eq_(djikstra.parse("(3+((3+3)+(3+3)))"), 3 * 5)
	eq_(djikstra.parse("(3*((3*3)*(3*3)))"), 3 ** 5)
	eq_(djikstra.parse("(9-((4-3)-(1-1)))"), 8)
	eq_(djikstra.parse("(8/((2/2)/(1/1)))"), 8)

def test_more_values_and_different_operators():
	djikstra = Djikstra()
	eq_(djikstra.parse("(3+(3*3))"), 12)
	eq_(djikstra.parse("(3+((3*3)+(3*3)))"), 21)
	eq_(djikstra.parse("(9+((4/2)*(9-3)))"), 21)
