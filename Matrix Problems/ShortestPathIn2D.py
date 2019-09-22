import collections
#23280666065765
class PointNode:
	def __init__(self, point, val):
		self.point = point
		self.dist = val

def shortestDistance(maze, start, destination):
	
	m=len(maze)
	n=len(maze[0])
	if start[0] > m or start[1] > n or destination[0] > m or destination[1] > n:
		return "Invalid Input"

	if not maze[start[0]][start[1]] or not maze[destination[0]][destination[1]]:
		return -1
	


	def isValid(r, c):
		# return the stop position and length
		if r >= 0 and r < m and c >= 0 and c < n:
			return True
		return False

	rows = [-1, 0, 0, 1]
	cols = [0, -1, 1, 0] 
	visited = {
		tuple(start): True
	}
	src = PointNode(start, 0)
	q = collections.deque()
	q.append(src)

	while q:
		curr = q.popleft()
		point = curr.point
		if point[0] == destination[0] and point[1] == destination[1]:
			return curr.dist
		
		for i in range(4):
			row = point[0] + rows[i]
			column = point[1] + cols[i]
			check_tuple = tuple([row, column])
			if isValid(row, column):
				if maze[row][column] and check_tuple not in visited:
					visited[check_tuple] = True
					node = PointNode([row,column], curr.dist + 1)
					q.append(node)
	return -1
	
print(shortestDistance([[0,0,1,1,1],[0,0,0,1,1],[0,0,0,1,1],[1,1,0,1,1],[0,0,0,1,1]], [0,4], [4,4]))
#Time Complexity is O(MN)