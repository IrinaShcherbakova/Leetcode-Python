class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = self.makeBoard(queens)
        # print(board)
        res = []
        row = self.sameRow(board, king)
        if len(row) > 0:
            res = res + row
        col = self.sameCol(board, king)
        if len(col) > 0:
            res = res + col
        diag = self.sameDiag(board, king)
        if len(diag) > 0:
            res = res + diag
        return res
    
    
    def sameRow(self, queens: List[List[int]], king: List[int])-> List[List[int]]:
        # print("same row: queen is %s" %queen)
        i, res = king[0], []
        for j in range(king[1]+1,8):
            if queens[i][j]:
                res.append([i,j])
                break
        for j in range(king[1]-1, -1, -1):
            if queens[i][j]:
                res.append([i,j])
                break
        return res
    
    
    def sameCol(self, queens: List[List[int]], king: List[int])-> List[List[int]]:
        # print("same col: queen is %s" %queen)
        j, res = king[1], []
        for i in range(king[0]+1,8):
            if queens[i][j]:
                res.append([i,j])
                break
        for i in range(king[0]-1, -1, -1):
            if queens[i][j]:
                res.append([i,j])
                break
        return res
    
    def sameDiag(self, queens: List[List[int]], king: List[int])-> List[List[int]]:
        # print("same diag: queen is %s" %queen)
        res = []
        north = self.checkNorth(queens, king)
        if len(north) > 0:
            res.append(north)
        west = self.checkWest(queens, king)
        if len(west) > 0:
            res.append(west)
        south = self.checkSouth(queens, king)
        if len(south) > 0:
            res.append(south)
        east = self.checkEast(queens, king)
        if len(east) > 0:
            res.append(east)
        return res
            
        
    #go in direction x-1, y+1
    def checkNorth(self, queens: List[List[int]], king: List[int])-> List[int]:
        # print("north: queen is %s" %queen)
        i, j = king[0]-1, king[1]+1
        while i >= 0 and j < 8:
            if queens[i][j]: #queen found
                return [i,j]
            i -= 1
            j += 1
        return []
    
    
    #go in direction x-1, y-1
    def checkWest(self, queens: List[List[int]], king: List[int])-> List[int]:
        # print("west: queen is %s" %queen)
        i, j = king[0]-1, king[1]-1
        while i >= 0 and j >= 0:
            if queens[i][j]: #obstacle found
                return [i,j]
            i -= 1
            j -= 1
        return []
    
    
    #go in direction x+1, y-1
    def checkSouth(self, queens: List[List[int]], king: List[int])-> List[int]:
        # print("south: queen is %s" %queen)
        i, j = king[0]+1, king[1]-1
        while i < 8 and j >= 0:
            if queens[i][j]: #obstacle found
                return [i,j]
            i += 1
            j -= 1
        return []
    
    
    #go in direction x+1, y+1
    def checkEast(self, queens: List[List[int]], king: List[int])-> List[int]:
        # print("east: queen is %s" %queen)
        i, j = king[0]+1, king[1]+1
        while i < 8 and j < 8:
            if queens[i][j]: #obstacle found
                return [i,j]
            i += 1
            j += 1
        return []
    
    
    def makeBoard(self, queens: List[List[int]])-> List[List[int]]:
        board = []
        for i in range(8):
            temp = [False]*8
            board.append(temp)
        for queen in queens:
            i, j = queen[0], queen[1]
            board[i][j] = True
        return board
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
