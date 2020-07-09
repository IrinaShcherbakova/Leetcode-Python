class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cells = len(board) * len(board[0])
        ships = 0
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[0]):
                if board[i][j] == 'X':
                    ships += 1
                    self.visitShip(board, i, j)
                j += 1
            i += 1
        return ships
            
                           
    def visitShip(self, board: List[List[str]], row: int, col: int) -> None:
        rows, cols = len(board), len(board[0])
        if row + 1 < rows and board[row+1][col] == 'X':
            return self.readCol(board, row, col)
        if col + 1 < cols and board[row][col+1] == 'X':
            return self.readRow(board, row, col)
        board[row][col] = '0'
        return 
    
    
    def readRow(self, board: List[List[str]], row: int, col: int) -> None:
        if row >= len(board) or col >= len(board[0]):
            return 
        start = col
        end = len(board[0])
        for j in range(start, end):
            if board[row][j] == 'X':
                board[row][j] = '0'
            else:
                return
        return
    
    
    def readCol(self, board: List[List[str]], row: int, col: int) -> None:
        if row >= len(board) or col >= len(board[0]):
            return 
        start = row
        end = len(board)
        for i in range(start, end):
            if board[i][col] == 'X':
                board[i][col] = '0'
            else:
                return 
        return 
        
    
    
    
    
    
        
