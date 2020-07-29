class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.expandIsland(grid, i, j)
        return islands
    
      
    def expandIsland(self, grid: List[List[str]], r: int, c: int) -> None:
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
            return None
        if grid[r][c] == '0':
            return None
        if grid[r][c] == '1':
            grid[r][c] = '2' #we visited this land
            self.expandIsland(grid, r+1, c)
            self.expandIsland(grid, r-1, c)
            self.expandIsland(grid, r, c+1)
            self.expandIsland(grid, r, c-1)
        return None
        
