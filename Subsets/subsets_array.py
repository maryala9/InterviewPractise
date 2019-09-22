def find_subsets(nums):
	subsets = []
	
	if not nums:
		return subsets
		
	subsets.append([])
	
	for num in nums:
		
		n = len(subsets)
		
		for i in range(n):
			
			temp = list(subsets[i])
			temp.append(num)
			subsets.append(temp)
			
	
	return subsets
	

def main():

	print("Here is the list of subsets: " + str(find_subsets([1, 3])))
	print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()