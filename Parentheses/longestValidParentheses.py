class Solution:
	def longestValidParentheses(self, s: str) -> int:
		
		if not s:
			return 0
		
		maxval = 0
		
		stack = [-1]
		
		for i in range(len(s)):
			
			if s[i] == '(':
				stack.append(i)
				
			else:
				stack.pop()
				
				if not stack:
					stack.append(i)
				else:
					maxval = max(maxval, i - stack[-1])
					
		return maxval