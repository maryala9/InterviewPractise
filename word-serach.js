#// Given a 2D board and a word, find if the word exists in the grid.
#
#// The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#// For example,
#// Given board =
#
#// word = "ABCCED", -> returns true,
#// word = "SEE", -> returns true,
#// word = "ABCB", -> returns false.
#// Hide Company Tags Microsoft Bloomberg Facebook
#// Hide Tags Array Backtracking
#// Hide Similar Problems (H) Word Search II


def search(board, row, col, word, index, visited):
	def is_valid(board, row, col):
		return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

	if not is_valid(board, row, col):
		return False
	if visited.__contains__((row, col)):
		return False
	if board[row][col] != word[index]:
		return False
	if index == len(word) - 1:
		return True

	visited.add((row, col))

	for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
		if search(board, row + d[0], col + d[1], word, index + 1, visited):
			return True

	visited.remove((row, col))  # Backtrack

	return False

def find_word(board, word):
	M = len(board)
	N = len(board[0])

	for row in range(M):
		for col in range(N):
			visited = set()
			if search(board, row, col, word, 0, visited):
				return True
	return False		
				
print(find_word( [
	['A','B','C','E'],
	['S','F','C','S'],
	['A','D','E','E']
	 ] , 'ABCCED'))


#//function exist(board, word) {
#//	var hash = {};
#//	var ans = [];
#//	for(var i = 0; i < board.length; i++) {
#//		for(var j = 0; j < board[0].length; j++) {
#//			if(dfs(board, word, 0, i, j)) {
#//				return true;
#//			}
#//		}
#//	}
#//	
#//	function dfs(board, word, w, i, j) {
#//		var key = i + ',' + j;
#//		if(hash[key]) {
#//			return false;
#//		}
#//		
#//		if(w === word.length) {
#////			console.log(ans);
#//			return true;
#//		}
#//		
#//		if(i < 0 || i >= board.length || j < 0 || j >= board[0].length) {
#//			return false;
#//		}
#//		
#//		var result = false;
#//		
#//		if(word[w] === board[i][j]) {
#//			hash[key] = true;
#////			ans.push([i,j]);
#//			result = dfs(board, word, w + 1, i+1, j) || dfs(board, word, w + 1, i-1, j) || dfs(board, word, w + 1, i, j+1) || dfs(board, word, w + 1, i, j-1);
#//			
#//			hash[key] = false;
#////			ans.pop();
#//		}
#//		
#//		return result
#//	}
#//	
#//	return false;
#//};
