
# code minesweeper? 
# 1. initialize board of X, Y, M
# 2. click(i, j) //tupple // start of dfs
#    a. mine, exploded
#    b. surrounded by mines (vertical, horizontal and diag), show the mine number
#       i. if there is no mines surrounds, if you need to repeatly click the surrounding cells.
# scott.shi@uber.com


# (2,2)
# empty space '#'
# mine exploded 'Z'
# 
import random

class Minesweeper():
    
    def __init__(self, x, y, mine_count):
        self.mine_count = mine_count
        self.board = [['b' for _ in range(x)] for _ in range(y)]
        
        mine = set([])
        
        for i in range(2*self.mine_count):
            rand = random.randint(1, x * y)
            if rand not in mine and len(mine) < self.mine_count:
                mine.add(rand)
                
        for rand in mine:
            self.board[rand % y][ rand // y] = 'm'
            
        # print(self.board)
        
    
    def click(self, x, y):
        m = len(self.board)
        n = len(self.board[0])
        return self.minesweeper(self.board, (x,y) , m, n)
        
    def minesweeper(self, board, click, x, y):
        if not board:
            return []
            
        i, j = click
        
        if board[i][j] == 'm':
            board[i][j] = 'Z'
            return board
            
        self.dfs(board, i, j, x, y)
        return board
    
        
    def dfs(self, board, i, j, x, y):
        if board[i][j] != 'b':
            return
        directions = [(-1,-1), (0, -1), (1,-1), (1,1), (1,0), (0,1), (-1, 1), (-1, 0)]
        count = 0
        for dirs in directions:
            
            a, b = i + dirs[0], j + dirs[1]
            
            if 0 <= a < x and 0 <=b < y and board[a][b] == 'm':
                count += 1
                
        if count ==0: 
            board[i][j] == '#'
        else:
            board[i][j] = str(count)
            return
        for dirs in directions:
            a, b = i + dirs[0], j + dirs[1]
            
            if 0 <= a < x and 0 <=b < y:
                self.dfs(board, a, b, x, y)
            

minsweep = Minesweeper(3,5,1)
print(minsweep.click(0,2))


# Minesweeper class takes input as row, columns, number of mines
# click function call with a given position

# Test Cases:
    
# 1. [[ 'b','b','b', 'b', 'b'],
# [ 'b', 'm', 'b', 'b', 'b'],
# [ 'b', 'm', 'b', 'b', 'b']] 

# 'b' - given un opened block
# 'm' - given mine
# '#' - empty space
# 'z' - 'Exploded'
# count -  number of mines around


#  changes are in just updating the board values, rest the program works as written before

# Result:
    # // When clicked on mine( 1,1) postiton we reveal as exploded at that block
    #  [['b', 'b', 'b', 'b', 'b'], ['b', 'Z', 'b', 'b', 'b'], ['b', 'b', 'b', 'b', 'b']]   
    
    # // when clicked at (0,2) position we reveal only one block and as its not mine  
        # [['b', 'b', '1', 'b', 'b'], ['b', 'm', 'b', 'b', 'b'], ['b', 'b', 'b', 'b', 'b']]
        
    
        
    
