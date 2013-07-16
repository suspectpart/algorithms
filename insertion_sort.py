class InsertionSort(object):
	'''
	Performs a little better than the selection sort algorithm because
	we stop swapping numbers as soon as the one to the right is bigger than the one to the left.
	This is especially useful when a list is already partially sorted.
	'''
	def sort(self, items):
		for i, item in enumerate(items):
			j = i
			while(j > 0):
				left, right = j-1, j
				if items[right] < items[left]:
					self.swap(items, left, right)
					j -= 1
				else:
					j = 0
		return items

	def swap(self, items, left, right):
		items[left], items[right] = items[right], items[left]