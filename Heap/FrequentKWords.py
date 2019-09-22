import collections,heapq 

#from collections import Counter
#class Solution:
#	def topKFrequent(self, words: List[str], k: int) -> List[str]:
#		return [x[0] for x in sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))][0:k]
#You're not going to get generally better runtime than the solution you've described. You have to do at least O(n) work to evaluate all the words, and then O(k) extra work to find the top k terms.
#
#If your problem set is really big, you can use a distributed solution such as map/reduce. Have n map workers count frequencies on 1/nth of the text each, and for each word, send it to one of m reducer workers calculated based on the hash of the word. The reducers then sum the counts. Merge sort over the reducers' outputs will give you the most popular words in order of popularity.
class Solution:
	def topKFrequent(self, words: List[str], k: int) -> List[str]:
		dic=collections.defaultdict(int)
		heap=[]
		for word in words:
			dic[word]+=1
			
		for key,val in dic.items():
			heapq.heappush(heap,(-val,key))

		res=[]
		while k:
			va,key=heapq.heappop(heap)
			res+=key,
			k-=1
		return res