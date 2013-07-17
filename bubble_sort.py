#test

def sort(items):
	for i in range(len(items)):
		for j, item in enumerate(items):
			if j < len(items) - 1 and item > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]
	return items
