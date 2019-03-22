def totalFruit(tree):
	count = {}
	i = res = 0
	for j, v in enumerate(tree):
		count[v] = count.get(v, 0) + 1
		print(count)
		while len(count) > 2:
			count[tree[i]] -= 1
			if count[tree[i]] == 0: del count[tree[i]]
			i += 1
		print(j, i)
		res = max(res, j - i + 1)
		print('res', res)
	return res
	
print(totalFruit([1,2,3,2,2]))