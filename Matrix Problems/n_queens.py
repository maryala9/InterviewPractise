class Solution:
	def __init__(self, N):
		self.cols = [0]*N
		self.diag = [0]*(2*N -1)
		self.antidiag = [0] * (2*N -1)
		self.queens = set()
		self.output = []
		self.N = N
		
	
	def can_place_queen(self, row, col):
		return not (self.cols[col] + self.diag[row - col] + self.antidiag[row+col])
		
	def place_queen(self, row, col):
		self.queens.add((row, col))
		self.cols[col] = 1
		self.diag[row-col] = 1
		self.antidiag[row + col] = 1
		
	def remove_queen(self, row, col):
		self.queens.remove((row, col))
		self.cols[col] = 0
		self.diag[row-col] = 0
		self.antidiag[row + col] = 0

	def add_solution(self):
		result = []
		
		for row, col in sorted(queens):
			self.output.append('.' * col + 'Q' + '.' * (n - col - 1))
		
	def backtrack(self, row = 0):
		
		for col in range(self.N):
			
			if self.can_place_queen(row, col):
				
				self.place_queen(row, col)
				
				if row  == self.N - 1:
					self.add_solution()
				else:
					self.backtrack(row+1)
				
				self.remove_queen(row, col)