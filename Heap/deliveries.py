import heapq
import math

class Solution:
	def kClosest(self, points, K):
		H = []
		heapq.heapify(H)
		for point in points:
			dist = self.distance(point[0], point[1])
			print(dist)
			if len(H) < K:
				heapq.heappush(H, (-dist , point))
				print("heap pushed")
			else:
				heapq.heappushpop(H, (-dist , point))
				print("heap popped")
				
			print(H)
				
		return [point for dist, point in H]    
		
		
	def distance(self,x, y):
		return x*x + y*y
		
s = Solution()
print(s.kClosest([[1,2],[-1,2],[2,3],[4,5]], 3))