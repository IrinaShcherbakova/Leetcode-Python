class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(9):
            if not self.checkRow(board, i):
                return False
        
        #check columns
        for i in range(9):
            if not self.checkCol(board, i):
                return False
            
        #check 3x3 boxes
        for i in range(3):
            for j in range(3):
                if not self.checkBox(board, i*3, j*3):
                    return False
        
        return True
    
    
    
    def checkRow(self, board: List[List[int]], row: int) -> bool:
        counts = [0] * 10
        for i in range(len(board[0])):
            cell = board[row][i]
            if cell != ".":
                num = int(cell)
                counts[num] += 1
                if counts[num] == 2:
                    return False
        return True
    
    
    def checkCol(self, board: List[List[int]], col: int) -> bool:
        counts = [0] * 10
        for i in range(len(board)):
            cell = board[i][col]
            if cell != ".":
                num = int(cell)
                counts[num] += 1
                if counts[num] == 2:
                    return False
        return True
   

    def checkBox(self, board: List[List[int]], row: int, col: int) -> bool:
        # print("row %s, col %s" %(row,col))
        counts = [0] * 10
        for i in range(3):
            for j in range(3):
                cell = board[row+i][col+j]
                if cell != ".":
                    num = int(cell)
                    counts[num] += 1
                    if counts[num] == 2:
                        return False
        return True
    
    
