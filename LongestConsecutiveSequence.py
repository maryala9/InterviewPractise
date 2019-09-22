# time complexity of O(N), and a space complexity of O(N).

def longest_consecutive(nums):
		max_len = 0
		bounds = dict()
		print(bounds)
		for num in nums:
			if num in bounds:
				continue
			left_bound, right_bound = num, num
			if num - 1 in bounds:
				left_bound = bounds[num - 1][0]
			if num + 1 in bounds:
				right_bound = bounds[num + 1][1]
			bounds[num] = left_bound, right_bound
			bounds[left_bound] = left_bound, right_bound
			bounds[right_bound] = left_bound, right_bound
			print(bounds)
			max_len = max(right_bound - left_bound + 1, max_len)

		return max_len
		
		
print(longest_consecutive([110,112,1,6,3,4,7,5,2,9,11,10,8]))