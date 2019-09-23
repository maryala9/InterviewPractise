class Solution:
	def subarraySum(self, nums, k: int) -> int:
		
		count = 0
		total = 0
		hash_map = {0: 1}
		
		for num in nums:
			total += num
			if total - k in hash_map:
				count += hash_map[total - k]
			if total in hash_map:
				hash_map[total] += 1
			else:
				hash_map[total] = 1
		
		return count