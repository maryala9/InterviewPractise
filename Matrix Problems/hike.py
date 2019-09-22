	# // Bob loves to go hiking, but refuses to ever go downhill. Given an NxM elevation map, determine if it is possible for Bob to get from point A to point B while only traversing from one point to the next without ever decreasing his elevation.

	#// 1 2 2 2
	#// 0 2 2 1
	#// 0 2 2 1
	#// 3 1 3 3
	#// (0,0) -> (3,3) => true
	#// 1 2 _ _
	#// _ 2 _ _
	#// _ 2 2 _
	#// _ _ 3 3

	#// (3,3) -> (0,0) => false
	#// _ _ _ _
	#// _ _ _ _
	#// _ _ _ _
	#// _ _ 3 3
#class Node:
#	 def __init__(self, val):
#		self.val = val
#		self.right = None
#		self.left = None
#	
#def detect_loop(head):
#	i = head
#	j = head.next.next
#	
#	while j.next:
#		
#		if i.val == j.val:
#			return True
#		
#		i = i.next
#		j = j.next
#		
#	return False
#	
		
	
def hike(board, start, end):
	
	if not board:
		return False
	
	start_x, start_y = start
	# directions = [(-1,0), (1,0), (0,-1), (0,1)]
	result = False
	visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
	
	for i in range(len(board)):
		for j in range(len(board[0])):
			if i == start_x and j == start_y:
				result = dfs(board, i, j, end, visited)
				break
	
	return result
				
				
def dfs(board, new_x, new_y, end, visited):            
	if new_x < 0 or new_x >len(board) or new_y < 0 or new_y > len(board[0]) or visited[new_x][new_y]:
		return False
	print(new_x, new_y)
	visited[new_x][new_y] = True
	temp = board[new_x][new_y]
	end_a , end_b = end
	if end_a == new_x and end_b == new_y:
		return True
	

			
	if new_x + 1 < len(board) and board[new_x +1][new_y] >= temp :
		val1 = dfs(board, new_x +1, new_y, end, visited)
		if val1:
			return True
	if new_x -1 > 0 and board[new_x -1][new_y] >= temp :
		val2 = dfs(board, new_x -1, new_y, end, visited)
		if val2:
			return True
	if new_y + 1 < len(board[0]) and board[new_x][new_y +1] >=temp:
		val3 = dfs(board, new_x, new_y +1, end, visited)
		if val3:
			return True
	if new_y -1 > 0 and board[new_x][new_y - 1] >= temp :
		val4 = dfs(board, new_x, new_y -1, end, visited)
		if val4:
			return True
		
#	if val1 or val2 or val3 or val4:
#		return True
	return False	
			
print(hike([[1,2,2, 2],[0, 2, 2, 1], [0, 2, 2, 1], [3, 1, 3, 3]], (0,0), (3,3)))
					
#// 1 2 2 2
#// 0 2 2 1
#// 0 2 2 1
#// 3 1 3 3
#// (0,0) -> (3,3) => true
#// 1 2 _ _
#// _ 2 _ _
#// _ 2 2 _
#// _ _ 3 3
				
					
					
					
					
					
		