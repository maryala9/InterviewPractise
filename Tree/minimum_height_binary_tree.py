# For maximum height of tree, just done have the check, keep incrementing the variable maximumDepthTree and return that when while loop ends

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_minimum_depth(root):
	if root is None:
		return 0

	queue = deque()
	queue.append(root)
	minimumTreeDepth = 0
	while queue:
		minimumTreeDepth += 1
		levelSize = len(queue)
		for _ in range(levelSize):
			currentNode = queue.popleft()

			# check if this is a leaf node
			if not currentNode.left and not currentNode.right:
				return minimumTreeDepth

			# insert the children of current node in the queue
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)



def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
	root.left.left = TreeNode(9)
	root.right.left.left = TreeNode(11)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()