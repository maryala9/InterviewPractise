class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def jump(self, nums):
		n = len(nums)
		start, end = 0, 0
		steps = 0
		maxfar = 0
		
		while end < n-1:
			steps += 1
			maxfar = end + 1
			
			for i in range(start, end + 1):
				if i + nums[i] >= n-1:
					return steps
				maxfar = max(maxfar, i + nums[i])
			
			start = end + 1
			end = maxfar
		
		return steps