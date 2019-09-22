class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if not s:
			return True
		result = []
		
		for i in s:
			
			if i == '(':
				result.append(')')
			elif i == '{':
				result.append('}')
			elif i == '[':
				result.append(']')
			elif not result or result.pop() != i:
				return False
		return True if not result else False