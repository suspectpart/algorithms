class SelectionSort():
	'''
	implemented in sedgewick style!
	'''
	def sort(self, items):
		for i, current in enumerate(items):
			smallest = i
			for j, value in enumerate(items[i+1:]):
				if value < items[smallest]:
					smallest = j+i+1
			items[i], items[smallest] = items[smallest], items[i]
		return items