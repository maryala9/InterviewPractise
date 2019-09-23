"""
# Definition for a Node.
"""
class Node(object):
	def __init__(self, val, next, random):
		self.val = val
		self.next = next
		self.random = random

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: Node
		:rtype: Node
		"""
		dic = collections.defaultdict(lambda: Node(self,0,0))
		dic[None] = None
		n = head
		while n:
			dic[n].val = n.val
			dic[n].next = dic[n.next]
			dic[n].random = dic[n.random]
			n = n.next
		return dic[head]