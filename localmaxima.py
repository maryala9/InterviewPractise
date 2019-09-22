def local_maximum(arr):
	n = len(arr)
	prev = arr[0]
	ln = 1 # length of the ascending sublist
	res = [] 
	for i in range(1,n,1):
		 if arr[i] >= prev:
			 ln += 1
		 else:
			if ln > 1:
	               res.append(prev)
				   ln = 1
		 prev = arr[i]
	# take care of the last sublist
if ln > 1:
	res.append(prev)
return res