class Solution:
	def __init__(self):
		self.result = []
	
	def generateParenthesis(self, n: int):
		
		if not n:
			return self.result
		
		self.backtrack(n, '', 0, 0)
		
		return self.result
		
	def backtrack(self, n, S, left, right):
		
		if len(S) == 2 * n:
			self.result.append(S)
			return
		
		if left < n:
			self.backtrack(n, S + '(', left +1, right)
		
		if right < left:
			
			self.backtrack(n, S + ')', left, right + 1)
			