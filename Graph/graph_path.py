def find_path(self, start_vertex, end_vertex, path=None):
	""" find a path from start_vertex to end_vertex 
		in graph """
	if path == None:
		path = []
	graph = self.__graph_dict
	path = path + [start_vertex]
	if start_vertex == end_vertex:
		return path
	if start_vertex not in graph:
		return None
	for vertex in graph[start_vertex]:
		if vertex not in path:
			extended_path = self.find_path(vertex, 
										   end_vertex, 
										   path)
			if extended_path: 
				return extended_path
	return None