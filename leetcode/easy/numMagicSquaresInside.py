class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.isMagic(grid, i, j):
                    res += 1
        return res
    
    
    def isMagic(self, grid: List[List[int]], row: int, col: int) -> bool:
        count = [0] * 10
        for i in range(3):
            for j in range(3):
                cur = grid[row+i][col+j]
                if cur > 9 or cur == 0:
                    return False
                count[cur] += 1
                if count[cur] > 1:
                    return False
        gridSum = grid[row][col] + grid[row][col+1] + grid[row][col+2]
        #check rows
        for i in range(1, 3):
            if grid[row+i][col] + grid[row+i][col+1] + grid[row+i][col+2] != gridSum:
                return False
        #check colums
        for i in range(3):
            if grid[row][col+i] + grid[row+1][col+i] + grid[row+2][col+i] != gridSum:
                return False
        #check diagonals
        if grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2] != gridSum:
            return False
        if grid[row+2][col] + grid[row+1][col+1] + grid[row][col+2] != gridSum:
            return False
        return True
           
