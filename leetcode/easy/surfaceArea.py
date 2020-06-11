class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:     
        #check 4 sides: for each adjeacent side - minus 1 unit
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                current = self.findPieceSurface(grid[i][j])
                #check east
                if j + 1 < cols and grid[i][j+1] > 0:
                    current = current - min(grid[i][j], grid[i][j+1])
                #check west
                if j - 1 >= 0 and grid[i][j-1] > 0:
                    current = current - min(grid[i][j], grid[i][j-1])
                #check north
                if i - 1 >= 0 and grid[i-1][j] > 0:
                    current = current - min(grid[i][j], grid[i-1][j])
                #check south
                if i + 1 < rows and grid[i+1][j] > 0:
                    current = current - min(grid[i][j], grid[i+1][j])
                res = res + current
        return res
                    
                                  
    def findPieceSurface(self, size: int) -> int:
        standard = 6
        if size == 1:
            return standard
        total = standard * size
        for i in range(size):
            if i == 0 or i == size - 1:
                total -= 1
            else:
                total -= 2
        return total
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
