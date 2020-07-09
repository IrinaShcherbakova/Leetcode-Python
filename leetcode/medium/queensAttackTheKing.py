class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = self.makeBoard(queens)
        # print(board)
        res = []
        for queen in queens:
            if self.sameRow(board, king, queen) or self.sameCol(board, king, queen) or self.sameDiag(board, king, queen):
                res.append(queen)
        return res
    
    
    def sameRow(self, queens: List[List[int]], king: List[int], queen: List[int])-> bool:
        # print("same row: queen is %s" %queen)
        if king[0] != queen[0]:
            return False
        start = (king[1] if king[1] < queen[1] else queen[1])
        end = (king[1] if king[1] > queen[1] else queen[1])
        i = king[0]
        for j in range(start+1, end):
            if queens[i][j]:
                return False
        return True
    
    
    def sameCol(self, queens: List[List[int]], king: List[int], queen: List[int])-> bool:
        # print("same col: queen is %s" %queen)
        if king[1] != queen[1]:
            return False
        start = (king[0] if king[0] < queen[0] else queen[0])
        end = (king[0] if king[0] > queen[0] else queen[0])
        j = king[1]
        for i in range(start+1, end):
            if queens[i][j]:
                return False
        return True
    
    
    def sameDiag(self, queens: List[List[int]], king: List[int], queen: List[int])-> bool:
        # print("same diag: queen is %s" %queen)
        return self.checkNorth(queens, king, queen) or self.checkWest(queens, king, queen) or self.checkSouth(queens, king, queen) or self.checkEast(queens, king, queen)
            
        
    #go in direction x-1, y+1
    def checkNorth(self, queens: List[List[int]], king: List[int], queen: List[int])-> bool:
        # print("north: queen is %s" %queen)
        i, j = king[0]-1, king[1]+1
        while i >= 0 and j < 8:
            if i == queen[0] and j == queen[1]:  #target queen found
                return True
            if queens[i][j]: #obstacle found
                return False
            i -= 1
            j += 1
        return False
    
    
    #go in direction x-1, y-1
    def checkWest(self, queens: List[List[int]], king: List[int], queen: List[int])-> bool:
        # print("west: queen is %s" %queen)
        i, j = king[0]-1, king[1]-1
        while i >= 0 and j >= 0:
            if i == queen[0] and j == queen[1]:
                return True
            if queens[i][j]: #obstacle found
                return False
            i -= 1
            j -= 1
        return False
    
    
    #go in direction x+1, y-1
    def checkSouth(self, queens: List[List[int]], king: List[int], queen: List[int])-> bool:
        # print("south: queen is %s" %queen)
        i, j = king[0]+1, king[1]-1
        while i < 8 and j >= 0:
            if i == queen[0] and j == queen[1]:
                return True
            if queens[i][j]: #obstacle found
                return False
            i += 1
            j -= 1
        return False
    
    
    #go in direction x+1, y+1
    def checkEast(self, queens: List[List[int]], king: List[int], queen: List[int])-> bool:
        # print("east: queen is %s" %queen)
        i, j = king[0]+1, king[1]+1
        while i < 8 and j < 8:
            if i == queen[0] and j == queen[1]:
                return True
            if queens[i][j]: #obstacle found
                return False
            i += 1
            j += 1
        return False
    
    
    def makeBoard(self, queens: List[List[int]])-> List[List[int]]:
        board = []
        for i in range(8):
            temp = [False]*8
            board.append(temp)
        for queen in queens:
            i, j = queen[0], queen[1]
            board[i][j] = True
        return board
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
