#Given a set of words (without duplicates), find all word squares you can build from them.
#
#A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
#For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
#
#```b a l l
#	a r e a
#	l e a d
#	l a d y
#```
#Note:
#There are at least 1 and at most 1000 words.
#All words will have the exact same length.
#Word length is at least 1 and at most 5.
#Each word contains only lowercase English alphabet a-z.

class PrefixHashTable(object):
	def __init__(self, words):
		self.prefix_table = {}
		for w in words:
			for prefix in (w[0:i] for i in range(len(w))):
				self.prefix_table.setdefault(prefix, set()).add(w)
		return
	
	def get_prefix_matches(self, prefix):
		candidates = self.prefix_table[prefix] if prefix in self.prefix_table else set([])        
		return candidates

class Solution(object):
	def helper(self, so_far, N, words, results, table):
		if len(so_far) == N:
			print("REsult so far", so_far)
			
			results.append([x for x in so_far])
			print("Result",results)
		else:
			print(so_far)
			prefix = "".join([x[len(so_far)] for x in so_far])
			print("prefix",prefix)
			for c in table.get_prefix_matches(prefix):
				print("char appending", c)
				so_far.append(c)
				self.helper(so_far, N, words, results, table)
				so_far.pop()
		return
	
	def wordSquares(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[str]]
		"""
		results = []
		if words:
			table = PrefixHashTable(words)
			# print(table)
			self.helper([], len(words[0]), words, results, table)
		return results