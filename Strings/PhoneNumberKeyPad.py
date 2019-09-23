class Solution:
	
	def __init__(self):
		self.output = []
		self.phone = {'2': ['a', 'b', 'c'],
				 '3': ['d', 'e', 'f'],
				 '4': ['g', 'h', 'i'],
				 '5': ['j', 'k', 'l'],
				 '6': ['m', 'n', 'o'],
				 '7': ['p', 'q', 'r', 's'],
				 '8': ['t', 'u', 'v'],
				 '9': ['w', 'x', 'y', 'z']}
		
	def letterCombinations(self, digits: str) -> list:
		if not digits:
			return self.output
		
		self.backtrack("", digits)
		
		return self.output
	
	def backtrack(self, string, digits):
		
		if len(digits) == 0:
			self.output.append(string)
		
		else:
			digit = digits[0]
			for letter in self.phone[digit]:
				self.backtrack(string + letter, digits[1:])