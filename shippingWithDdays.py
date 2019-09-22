def shipDays(arr, d):
	
	low = max(arr)
	high = sum(arr)
	
	while low < high:
		
		mid = (low + high) // 2
		total = 0
		res = 1
		
		for weight in arr:
			if total + weight > mid:
				total = weight
				res += 1
			else:
				total += weight
			
		if res <= d:
			print(res, mid)
			high = mid
		else: 
			low = mid +1
			
	return low
	

print(shipDays([1,2,3,4,5,6,7,8,9,10], 5)) 