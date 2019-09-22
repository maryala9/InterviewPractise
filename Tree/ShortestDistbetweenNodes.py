class NewNode:
	
	def __init__(self, key):
		self.val = key
		self.right = None
		self.left = None
		
	
def insert(root, key):
	
	if root==None:
		root = NewNode(key)
	elif root.val > key:
		root.left = insert(root.left, key)	
	elif root.val < key:
		root.right = insert(root.right, key)
	return root
	
	
def findDistWrapper(root, a, b):
	if a > b:
		a,b = b,a
	return distanceBetween2(root, a, b) 


def height(root, key):
	
	if root.val == key:
		return 0
	elif root.val > key:
		return 1 + height(root.left, key)
	else:
		return 1 + height(root.right, key) 

def distanceBetween2(root, a, b):
	
	if root == None:
		return 0
		
	if root.val < a and root.val < b:
		return distanceBetween2(root.right, a, b)
	
	if root.val > a and root.val > b:
		return distanceBetween2(root.left, a, b)	
	
	if root.val >= a and root.val <= b:
		return (height(root, a) + height(root, b))
		
	
if __name__ == '__main__': 
	root = None
	root = insert(root, 20)  
	insert(root, 10)  
	insert(root, 5)  
	insert(root, 15)  
	insert(root, 30)  
	insert(root, 25)  
	insert(root, 35) 
	a, b = 5, 55
	print(findDistWrapper(root, 5, 35))  