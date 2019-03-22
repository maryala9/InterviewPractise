class Solution(object):
#					('abab', 'xyzabcxyzabc')
	def match(self, pattern, str, r1, r2):
		if not (pattern or str):
			return True

		if not pattern and str or pattern and not str:
			print('sdecinf ')
			return False

		char = pattern[0]
		coun = 0
		print('main')
		for j in range(len(str)):
			substr = str[:j + 1]
			print("char:", substr)
			if char not in r1 and substr not in r2:
				print('loop')
				r1[char] = substr
				print('r1:', r1)
				r2[substr] = char
				print('r2:', r2)
				if self.match(pattern[1:], str[j + 1:], r1, r2):
#					print(r1, r2)
					return True

				del r1[char]
				del r2[substr]

			elif (char in r1 and r1[char] == substr and
					self.match(pattern[1:], str[j + 1:], r1, r2)):
				return True

		return False

	def wordPatternMatch(self, pattern, str):
		r1, r2 = {}, {}
		return self.match(pattern, str, r1, r2)


s = Solution()
print(s.wordPatternMatch('abab', 'xyzabcxyzabc'))