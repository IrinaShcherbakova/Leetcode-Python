class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited_zeros = []
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == 'O' and board[i-1][j] == 'X' and board[i][j-1] == 'X':
                    visited = []
                    is_region = self.capture_region(board, i, j, visited)
                    for pos in visited:
                        r, c = pos[0], pos[1]
                        board[r][c] = ('X' if is_region else 'O')                
       
        return
    
    
    #expand region right and down
    def capture_region(self, board: List[List[str]], row: int, col: int, visited: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        
        if board[row][col] == 'X' or board[row][col] == 'V':
            return True
         
        if (row == 0 or row == len(board)-1) and board[row][col] == 'O':
            return False
        if (col == 0 or col == len(board[0])-1) and board[row][col] == 'O':
            return False
     
        board[row][col] = 'V'
        visited.append([row,col])
        top = self.capture_region(board, row-1, col, visited)
        if not top:
             return False
        bottom = self.capture_region(board, row+1, col, visited)
        if not bottom:
            return False
        right = self.capture_region(board, row, col+1, visited)
        if not right:
            return False
        left = self.capture_region(board, row, col-1, visited)
        if not left:
            return False   

        return True
    
    
    
    
    
    
