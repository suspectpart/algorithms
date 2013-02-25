class BinarySearch(object):
	def __init__(self, numbers):
		self.numbers = numbers
	def search(self, number):
		lo, hi = 0, len(self.numbers) - 1
		
		while lo <= hi:
			mid = lo + (hi-lo) / 2
			if number < self.numbers[mid]:
				hi = mid - 1
			elif number > self.numbers[mid]:
				lo = mid + 1
			else:
				return mid
		return -1
