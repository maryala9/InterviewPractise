from heapq import *

def find_k_elements(nums, k) -> list:
	
	if not nums or not k:
		return []
		
	min_heap = []
	
	for i in range(k):
		heappush(min_heap, nums[i])
		
	for i in range(k, len(nums)):
		
		if nums[i] > min_heap[0]:
			
			heapreplace(min_heap, nums[i])
			
	return list(min_heap)
	

def main():

	print("Here are the top K numbers: " +
				str(find_k_elements([3, 1, 5, 12, 2, 11], 3)))

	print("Here are the top K numbers: " +
				str(find_k_elements([5, 12, 11, -1, 12], 3)))


main()