def max_subarray_sum(arr):
	if not arr:
		return 0
	
	curr_sum = max_sum = arr[0]
	
	for num in arr[1:]:
		
		curr_sum = max(num, curr_sum + num)
		max_sum = max(max_sum, curr_sum)
	
	return max_sum
	
		
print(max_subarray_sum([-2,-1,-3,-4,-1,-2,-1,-5,4]))