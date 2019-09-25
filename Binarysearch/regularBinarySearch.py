def binary_search(arr, key):
	
	if not arr:
		return None
		
	start = 0
	end = len(arr) - 1
	
	while start <= end:
		
		mid = start + (end - start)//2
		
		if key == arr[mid]:
			return mid
		
		if key < arr[mid]:
			end = mid - 1
		else:
			start = mid + 1
			
	return -1
	

def main():
	print(binary_search([4, 6, 10], 6))
	print(binary_search([1, 2, 3, 4, 5, 6, 7,8], 5))
	


main()