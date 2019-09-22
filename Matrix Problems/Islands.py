class Solution(object):
	def numIslands(self, grid):

		if not grid or not grid[0]:
			return 0
		
		count = 0
		
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] == '1':
					self.dfs(grid, row, col)
					count += 1
		return count
	
	def dfs(self, grid, row, col):
		if (row < 0 or col < 0) or (row >= len(grid) or col >= len(grid[0])) or grid[row][col] != '1':
			return
		grid[row][col] = '#'
		self.dfs(grid, row + 1, col)
		self.dfs(grid, row - 1, col)
		self.dfs(grid, row, col + 1)
		self.dfs(grid, row, col - 1)
		
