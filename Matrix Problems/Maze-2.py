import heapq
def shortestDistance(maze, start, destination):
	"""
	:type maze: List[List[int]]
	:type start: List[int]
	:type destination: List[int]
	:rtype: int
	"""
	dest=tuple(destination)
	m=len(maze)
	n=len(maze[0])
	res=None 
	def go(start, direction):
		# return the stop position and length
		i, j = start
		ii, jj = direction
		l=0
		while 0<=i+ii<m and 0<=j+jj<n and maze[i+ii][j+jj]!=1:
			i+=ii
			j+=jj
			l+=1
		return l, (i,j)
	# bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
	visited={}
	q=[]
	heapq.heappush(q, (0, tuple(start)))
	while q:
		length, cur = heapq.heappop(q)
		if cur in visited and visited[cur]<=length:
			continue # if cur is visited and with a shorter length, skip it.
		visited[cur]=length
		if cur == dest:
			return length
		for direction in [(-1, 0), (1, 0), (0,-1), (0,1)]:
			l, np = go(cur, direction)
			heapq.heappush(q, (length+l, np))
	return -1
	
print(shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4]))