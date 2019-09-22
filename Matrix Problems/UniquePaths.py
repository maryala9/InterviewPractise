class UniquePaths:	
	def unique_paths(m,n):
		
		if m==0 or n==0:
			return 0
		
		dp = [[0]*n]*m
		
		dp[0][0] = 1
		
		for i in range(1,m):
			dp[i][0] = 1
		
		for i in range(1, n):
			dp[0][i] = 1
			
		for i in range(1, m):
			for j in range(1,n):
				dp[i][j] = dp[i][j-1] + dp[i-1][j]
				
		return dp[m][n]