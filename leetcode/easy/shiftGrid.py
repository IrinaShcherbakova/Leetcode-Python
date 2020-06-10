class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        cols = len(grid[0])
        rows = len(grid)
        #locate new start row and column
        totalCells = cols * rows
        k = k % totalCells
        newRow = 0
        while k > cols:
            k = k - cols
            newRow += 1
        newCol = k
        
        #shift all elements to new position starting from grid[m-1][n-1]
        res = []
        row = 0
        while row < rows:
            res.append([None]*cols)
            row += 1
        for row in grid:
            for num in row:
                print(num)
                if newCol == cols:
                    newCol = 0
                    if newRow == rows - 1:
                        newRow = 0
                    else:
                        newRow += 1
                res[newRow][newCol] = num
                newCol += 1
        return res
                
                        
        
        
        
