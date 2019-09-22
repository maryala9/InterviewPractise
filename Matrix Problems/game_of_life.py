def game_of_life(board):
	if not board:
		return None
	
	dp = []
	m = len(board)
	n = len(board[0])
	for i in m:
		dp.append([])
	moves = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
	for i in m:
		for j in n:
			item = board[i][j]
			count = 0
			for k in moves:
				a,b = k
				x = i + a
				y = j + b
				
				if x < 0 or x >= m or y < 0 or y >= n:
					continue
				count += board[x][y]
			
			if item:
				dp[i][j] = 1 if count ==2 or count == 3 else 0
			else:
				dp[i][j] = 1 if count == 3 else 0
	
	for i in m:
		for j in n:
			board[i][j] = dp[i][j] 
				
				