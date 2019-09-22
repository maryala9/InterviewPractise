def max_sum_subarray(K, arr):
	
	if not arr or not K:
		return 0
	
	start = 0
	total = 0.0
	max_sum = 0
	for end in range(len(arr)):
		
		total += arr[end] 
		if end >= K - 1:
			max_sum = max(max_sum, total)
			total -= arr[start]
			start += 1
	
	return max_sum
	
#res = max_sum_subarray(3, [2, 1, 5, 1, 3, 2])
res = max_sum_subarray(2, [2, 3, 4, 1, 5])

print(res)