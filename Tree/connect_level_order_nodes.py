from __future__ import print_function
from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right, self.next = None, None, None

	# level order traversal using 'next' pointer


def connect_level_order_siblings(root):
	if root is None:
		return

	queue = deque()
	queue.append(root)
	while queue:
		previousNode = None
		levelSize = len(queue)
		# connect all nodes of this level
		for _ in range(levelSize):
			currentNode = queue.popleft()
			if previousNode:
				previousNode.next = currentNode
			previousNode = currentNode

			# insert the children of current node in the queue
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	connect_level_order_siblings(root)

	print("Level order traversal using 'next' pointer: ")



main()