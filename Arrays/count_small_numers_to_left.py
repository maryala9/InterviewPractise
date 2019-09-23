class Item:
	def __init__(self, val, index):
		self.val = val
		self.index = index
		

def count_smaller_numbers(nums):
	n = len(nums)
	
	items = []
	
	for i in range(n):
		items.append(Item(nums[i], i))
	
	count = []
	
	mergeSort(items, 0, n-1, count)
	
	res = []
	
	for c in count:
		res.append(c)
		
	return res
	

def mergeSort(items, low, high, count):
	
	if low >= high:
		return
	
	mid = low + (high - low)//2
	
	mergeSort(items, low, mid, count)
	mergeSort(items, mid + 1, high, count)
	merge(items, low, mid, mid +1, high, count)
	

def merge(items, low, lowEnd, high, highEnd, count):
	
	m = highEnd - low + 1
	
	sorted_result = []
	
	index = 0
	lowPtr = low
	highPtr = high
	
	rightCounter = 0
	
	while (lowPtr <= lowEnd and highPtr <= highEnd):
		if items[highPtr].val < items[lowPtr].val:
			rightCounter += 1
			sorted_result.append(items[highPtr])
			highPtr += 1
		else:
			count[items[lowPtr].index] += rightCounter
			sorted_result.append(items[lowPtr])
			lowPtr += 1
	
	while lowPtr <= lowEnd:
		count[items[lowPtr].index] += rightCounter
		sorted_result.append(items[lowPtr])
		lowPtr += 1
	
	while highPtr <= highEnd:
		sorted_result.append(items[highPtr])
		highPtr += 1

	
	