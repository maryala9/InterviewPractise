// Given a 2D board and a word, find if the word exists in the grid.

// The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

// For example,
// Given board =

// word = "ABCCED", -> returns true,
// word = "SEE", -> returns true,
// word = "ABCB", -> returns false.
// Hide Company Tags Microsoft Bloomberg Facebook
// Hide Tags Array Backtracking
// Hide Similar Problems (H) Word Search II


function exist(board, word) {
	var hash = {};
	var ans = [];
	for(var i = 0; i < board.length; i++) {
		for(var j = 0; j < board[0].length; j++) {
			if(dfs(board, word, 0, i, j)) {
				return true;
			}
		}
	}
	
	function dfs(board, word, w, i, j) {
		var key = i + ',' + j;
		if(hash[key]) {
			return false;
		}
		
		if(w === word.length) {
//			console.log(ans);
			return true;
		}
		
		if(i < 0 || i >= board.length || j < 0 || j >= board[0].length) {
			return false;
		}
		
		var result = false;
		
		if(word[w] === board[i][j]) {
			hash[key] = true;
//			ans.push([i,j]);
			result = dfs(board, word, w + 1, i+1, j) || dfs(board, word, w + 1, i-1, j) || dfs(board, word, w + 1, i, j+1) || dfs(board, word, w + 1, i, j-1);
			
			hash[key] = false;
//			ans.pop();
		}
		
		return result
	}
	
	return false;
};
console.log(exist( [
	['A','B','C','E'],
	['S','F','C','S'],
	['A','D','E','E']
 ]
, 'CBAS'))