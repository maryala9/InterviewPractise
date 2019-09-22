def flatten_array(arr):
	res = []
	
	while len(arr):
		i = arr.pop(0)
		
		if isinstance(i, list):
			arr = i + arr
		else:
			res.append(i)
	
	return res
	

print(flatten_array([1,[4,[3]],[6]]))

def flatten_tupple(tup):
	res = ()
	
	for item in tup:
			

print(flatten_tupple(('E', ('B', ('A', ())))))