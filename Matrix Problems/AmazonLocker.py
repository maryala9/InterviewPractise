import collections
def find_distance(matrix):
	m = len(matrix)
	n = len(matrix[0])
	output = [[None for _ in range(n)] for _ in range(m)]
	queue = collections.deque([])
	row = [-1, 0, 1, 0]
	col = [0, 1, 0, -1]
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 'L':
				queue.append((i, j, 0))
				output[i][j] = 0
	
	while queue:
		
		curr_i, curr_j, dist = queue.popleft()
		
		for i in range(4):
			x = curr_i + row[i]
			y = curr_j + col[i]
			
#			print(x,y)
			if x >=0 and y >=0 and x < m and y < n and matrix[x][y] != 'L' and output[x][y] is None:
				output[x][y] = dist + 1
				queue.append((x, y, dist + 1))
			else:
				continue
	return output
	
print(find_distance([[0, 0, 0, 'L'],  [0, 0, 'L', 'L'], [0, 0, 0, 0]]))
