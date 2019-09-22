import collections

class Solution:
	def removeInvalidParentheses(self, s: str) -> list:
		
		visited = {}
		queue = collections.deque([s])
		
		result = []
		found = False
		while queue:
			
			temp = queue.popleft()
			
			if self.valid(temp):
				result.append(temp)
				found = True
				
#             If we forund a valid one then again dont iterate on it , because it will iterate to its subsets- Question is for minimum number to delete
			if found:
				continue
				
			
			for i in range(len(temp)):

				if temp[i].isalpha():
					continue

				curr = temp[:i] + temp[i+1:]

				if curr not in visited:
					visited[curr] = True
					queue.append(curr)
						
			
		return result
					
		
	
	def valid(self, s):
		
		count = 0
		
		for c in s:
			
			if c == '(':
				count += 1
			
			elif c == ')':
				count -= 1
				
			if count < 0:
				return False
			
		return count == 0
		