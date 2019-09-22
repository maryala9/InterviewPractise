#//Can have negatives or floating points

def average_subarray(arr, K):
	
	result = []
	
	if not arr or not K:
		return arr
	
	start = 0
	total = 0.0
	
	for end in range(len(arr)):
		
		total += arr[end] 
		if end >= K - 1:
			result.append(total/K)
			total -= arr[start]
			start += 1
	
	return result


res = average_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)

print(res)