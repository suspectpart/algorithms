class SelectionSort():
	'''
	implemented sedgewick style!
	
	As we always have to loop because we can't know where the minimum item is,
	this algorithm will always perform ~ N^2 / 2 compares, no matter if the input is already sorted or not.
	That sucks because - as sedgewick told us - quadratic time is no good.
	'''
	def sort(self, items):
		for i, current in enumerate(items):
			smallest = i
			for j, value in enumerate(items[i+1:]):
				if value < items[smallest]:
					smallest = j+i+1
			items[i], items[smallest] = items[smallest], items[i]
		return items