class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		if len(obstacleGrid) == 1:
			if [1] not in obstacleGrid[0]:
				return 1
			else: 
				return 0
		if len(obstacleGrid[0]) == 1:
			if [1] not in obstacleGrid:
				return 1
			else: 
				return 0
		
		if obstacleGrid[0][0] == 1:
			return 0
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		dp = [[0]*n]*m
		dp[0][0] = 1
		
		for i in range(1, m):
			if obstacleGrid[i][0] == 1:
		 		dp[i][0] = 0
			else:
				dp[i][0] = dp[i-1][0]
		for j in range(1, n):
			if obstacleGrid[0][j] == 1:
				dp[0][j] = 0
			else:
				dp[0][j] = dp[0][j-1]
		
		for i in range(1, m):
			for j in range(1, n):
				if obstacleGrid[i][j] == 1:
					dp[i][j] = 0
				else:
					dp[i][j] = dp[i-1][j] + dp[i][j-1]
					
		
		return dp[-1][-1]
		
		
s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))	
