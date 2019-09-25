class Solution:
	def canJump(self, nums: List[int]) -> bool:
		lenN = len(nums)
		if lenN == 1:
			return True
		leftmost =  lenN - 1
		for i in range(lenN-1,-1,-1):
			if i + nums[i] >= leftmost:
				leftmost = i
		return leftmost == 0