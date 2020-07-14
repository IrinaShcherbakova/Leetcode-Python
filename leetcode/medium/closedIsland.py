class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        islands = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                # print("cell %s %s, value %s" %(i, j, grid[i][j]))
                if grid[i][j] == 0 and self.isIsland(grid, i, j):
                    islands += 1
                    # print("%s islands from %s %s" %(islands, i, j))
        return islands
                
    
    def isIsland(self, grid: List[List[int]], r: int, c: int) -> bool:
        if r < 0 or r >= len(grid):
            return False
        if c < 0 or c >= len(grid[0]):
            return False
        if grid[r][c] == 1 or grid[r][c] == 2:
            return True
        grid[r][c] = 2
        right = self.isIsland(grid, r, c+1)
        left = self.isIsland(grid, r, c-1) 
        top = self.isIsland(grid, r-1, c)
        bottom = self.isIsland(grid, r+1, c)
        return right and left and top and bottom
       
        
        
        
        
