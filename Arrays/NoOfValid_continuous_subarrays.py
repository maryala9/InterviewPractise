"""
Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.
"""

class Solution:
	def validSubarrays(self, nums) -> int:
		n = len(nums)
		stack = []
		ans = 0
		for i,num in enumerate(nums):
			while stack and num<nums[stack[-1]]:
				ind = stack.pop()
				ans += i-ind
			stack.append(i)
		while stack:
			ind = stack.pop()
			ans+=n-ind
		return ans