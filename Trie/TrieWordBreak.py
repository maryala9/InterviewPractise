class TrieNode(object):
	def __init__(self, char=None, isWord=False):
		self.char = char
		self.isWord = isWord
		self.children = {}


class Trie(object):
	def __init__(self):
		self.root = TrieNode()
		self.cache = {}

	def insert(self, word):
		root = self.root
		for char in word:
			if char not in root.children:
				root.children[char] = TrieNode(char)
			root = root.children[char]
		root.isWord = True

	def cache(f):
		def method(obj, s):
			if s not in obj.cache:
				obj.cache[s] = f(obj, s)
			return obj.cache[s]
		return method

	@cache
	def search(self, s):
		root = self.root
		for i, char in enumerate(s):
			if char not in root.children:
				return False

			if root.children[char].isWord:
				if self.search(s[i + 1:]):
					return True
			root = root.children[char]
		return root.isWord


class Solution(object):
	def wordBreak(self, s, wordDict):
		trie = Trie()
		[trie.insert(word) for word in wordDict]

		return trie.search(s)