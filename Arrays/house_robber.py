def circl_house(nums):
	if not nums:
		return 0
	if len(nums) <= 2:
		return max(nums)
	
	return max(house_robber(nums[1:]), house_robber(nums[:-1]))



def house_robber(nums):
	
	if not nums: 
		return 0
		
	odd = 0
	even = 0
	
	for i in range(len(nums)):
		
		if i%2 == 0:
			even = max(odd, nums[i] + even)
		else:
			odd = max(even, nums[i] + odd)
			
	return max(even, odd)