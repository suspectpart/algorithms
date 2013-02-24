from nose.tools import *
from union_quick_union import UnionFind

def test_connected():
	union = UnionFind(3)
	assert_equals(union.connected(0,1), False)
	assert_equals(union.connected(1,2), False)
	union.union(0,1)
	assert_equals(union.connected(0,1), True)
	assert_equals(union.connected(1,2), False)
	union.union(1,2)
	assert_equals(union.connected(2,0), True)
	assert_equals(union.connected(0,2), True)
	assert_equals(union.connected(1,2), True)