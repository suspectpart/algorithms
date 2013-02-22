from union_weighted_union import UnionFind

def test_connected():
	union = UnionFind(3)
	assert union.connected(0,1) == False
	assert union.connected(1,2) == False
	union.union(0,1)
	assert union.connected(0,1)
	assert union.connected(1,2) == False
	union.union(1,2)
	assert union.connected(2,0)
	assert union.connected(0,2)
	assert union.connected(1,2)