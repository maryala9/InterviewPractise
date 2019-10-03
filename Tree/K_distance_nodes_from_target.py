class Solution:
	def distanceK(self, root, target, K):
		adj, res, visited = collections.defaultdict(list), [], set()
		def dfs(node):
			if node.left:
				adj[node].append(node.left)
				adj[node.left].append(node)
				dfs(node.left)
			if node.right:
				adj[node].append(node.right)
				adj[node.right].append(node)
				dfs(node.right)
		dfs(root)
		def dfs2(node, d):
			if d > K:
				return
			if d < K:
				visited.add(node)
				for v in adj[node]:
					if v not in visited:
						dfs2(v, d + 1)
			else:
				res.append(node.val)
		dfs2(target, 0)
		return res
		