class BinarySearch(object):
	def __init__(self, numbers):
		self.numbers = numbers
	def search(self, number):
		return self._search(number, lo = 0, hi = len(self.numbers) -1)
	def _search(self, number, lo, hi):
		if lo > hi:
			return -1
		mid = lo + (hi-lo) / 2
		if number < self.numbers[mid]:
			return self._search(number, lo, hi = mid - 1)
		if number > self.numbers[mid]:
			return self._search(number, lo = mid + 1, hi)
		return mid