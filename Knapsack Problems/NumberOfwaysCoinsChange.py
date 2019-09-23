def coins_change(amount, coins):
	
	dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+ 1)]
	
	dp[0][0] = 1
	
	for i in range(len(coins) + 1):
		dp[i][0] = 1
		for j in range(1, amount+1):
			
			if i -1 < 0:
				without_using_val = 0
				dp[i][j] = 0 + 0
			else:
				dp[i][j] = dp[i-1][j] + dp[i][j - coins[i -1]]
			
	
	return dp[len(coins)][amount]
	

print(coins_change(5, [1,2,5]))
print(coins_change(10, [5]))