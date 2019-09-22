from heapq import *


def find_closest_points(points, K) -> list:
	
	distance = []
	for i in points:
		heappush(distance,(i[0]**2+i[1]**2,i))
	K_points = []
	for i in range(K):
		K_points.append(heappop(distance)[1])
	return K_points
	

def main():

	result = find_closest_points([(1, 3), (3, 4), (2, -1)], 2)
	print("Here are the k points closest the origin: ", end='')
	print(result)


main()