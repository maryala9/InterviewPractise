class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		if not heights:
			return 0
		# non-decreasing stack
		ans = 0
		stack = []
		
		# while scanning
		for j in range(len(heights)):
			while stack and heights[stack[-1]] > heights[j]:
				print('stack', stack)
				kick = stack.pop()
				print('kick', kick)
				left = 0 if not stack else stack[-1]+1
				print('left', left, j)
				ans = max(ans, heights[kick] * (j - left))
				print(ans)
			stack.append(j)

		# cleanup
		n = len(heights)
		while stack:
			kick = stack.pop()
			last = 0 if not stack else stack[-1] + 1
			ans = max(ans, heights[kick] * (n - last))

		return ans