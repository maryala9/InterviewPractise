from heapq import *

def find_Kth_smallest_number(nums, k) -> int:
	
	if not nums:
		return -1
		
		
	min_heap = []
	
	for i in range(k):
		heappush(min_heap, -nums[i])
		
	for i in range(k, len(nums)):
		if -nums[i] > min_heap[0]:
			heapreplace(min_heap, -nums[i])
		
	
	return -min_heap[0]
	

def main():

	print("Kth smallest number is: " +
				str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

	# since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
	print("Kth smallest number is: " +
				str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

	print("Kth smallest number is: " +
				str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()