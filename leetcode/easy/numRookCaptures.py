[200~class Solution:
            def numRookCaptures(self, board: List[List[str]]) -> int:
                    rowR = colR = 0
                            #locate the white rook
                                    for i in range(len(board)):
                                                isFound = False
                                                            for j in range(len(board[i])):
                                                                            if board[i][j] == 'R':
                                                                                                rowR = i
                                                                                                                    colR = j
                                                                                                                                        isFound = True
                                                                                                                                                    if isFound:
                                                                                                                                                                    break
                                                                                                                                                                            return self.scanRow(board[rowR], colR) + self.scanColumn(board, rowR, colR)
                                                                                                                                                                                    
                                                                                                                                                                                def scanColumn(self, board: List[List[str]], row: int, col: int) -> int: 
                                                                                                                                                                                        res = 0
                                                                                                                                                                                                i = row-1
                                                                                                                                                                                                        while i >= 0:
                                                                                                                                                                                                                    if board[i][col] == 'B':
                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                elif board[i][col] == 'p':
                                                                                                                                                                                                                                                                res += 1
                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                            i -= 1
                                                                                                                                                                                                                                                                                                                    i = row+1
                                                                                                                                                                                                                                                                                                                            while i < len(board):
                                                                                                                                                                                                                                                                                                                                        if board[i][col] == 'B':
                                                                                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                                                                                                    elif board[i][col] == 'p':
                                                                                                                                                                                                                                                                                                                                                                                    res += 1
                                                                                                                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                i += 1
                                                                                                                                                                                                                                                                                                                                                                                                                                        return res
                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                            def  scanRow(self, row: List[str], col: int) -> int: 
                                                                                                                                                                                                                                                                                                                                                                                                                                                    res = 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                            i = col-1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    while i >= 0:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if row[i] == 'B':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            elif row[i] == 'p':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            res += 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        i -= 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                i = col+1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        while i < len(row):
                if row[i] == 'B':
                                    break
                                            elif row[i] == 'p':
                                                                res += 1
                                                                                break
                                                                                        else:
                                                                                                            i += 1
                                                                                                                    return res
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rowR = colR = 0
        #locate the white rook
        for i in range(len(board)):
            isFound = False
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    rowR = i
                    colR = j
                    isFound = True
            if isFound:
                break
        return self.scanRow(board[rowR], colR) + self.scanColumn(board, rowR, colR)
        
    def scanColumn(self, board: List[List[str]], row: int, col: int) -> int: 
        res = 0
        i = row-1
        while i >= 0:
            if board[i][col] == 'B':
                break
            elif board[i][col] == 'p':
                res += 1
                break
            else:
                i -= 1
        i = row+1
        while i < len(board):
            if board[i][col] == 'B':
                break
            elif board[i][col] == 'p':
                res += 1
                break
            else:
                i += 1
        return res
         
        
    def  scanRow(self, row: List[str], col: int) -> int: 
        res = 0
        i = col-1
        while i >= 0:
            if row[i] == 'B':
                break
            elif row[i] == 'p':
                res += 1
                break
            else:
                i -= 1
        i = col+1
        while i < len(row):
            if row[i] == 'B':
                break
            elif row[i] == 'p':
                res += 1
                break
            else:
                i += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
