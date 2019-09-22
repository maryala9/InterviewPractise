class LRUCache:
	def __init__(self, capacity):
		from collections import deque
		self.capacity = capacity
		self.dic = {}
		self.deque = deque([])
 
	def get(self, key):
		if key not in self.dic: return -1
		self.deque.remove(key)
		self.deque.append(key)
		return self.dic[key]


	def put(self, key, value):
		if key in self.dic:
			self.deque.remove(key)
			self.deque.append(key)
			self.dic[key] = value
		elif len(self.dic) == self.capacity:
			val = self.deque.popleft()
			self.dic.pop(val)
			self.deque.append(key)
			self.dic[key] = value
		else:
			self.deque.append(key)
			self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)