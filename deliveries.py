import math
import heapq

def delivery_locations(destinations, all_locations, numDeliveries):
	if not numDeliveries or numDeliveries > len(all_locations):
		return "Can not Deliver"
	source = [0,0]
	q = []
	dist_map = {}
	def compute_distance(dest):
		return math.pow(dest[0], 2) + math.pow(dest[1],2)
	
	for i in all_locations:
		dist = compute_distance(i)
		if dist not in dist_map:
			dist_map[dist] = [i]
			heapq.heappush(q, dist)
		else:
			dist_map[dist].append(i)
	
	result = []
	
	while q:
		current = heapq.heappop(q)
		delivery = dist_map[current]
		for point in delivery:
			if len(result) >= numDeliveries:
				break
			result.append(point)
		
	return result	
		
		
print(delivery_locations(4, [[1,2], [-1,2],[2,3],[4,5]], 2))