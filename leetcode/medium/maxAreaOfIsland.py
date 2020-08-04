class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.explore_island(grid, i, j)
                    maxArea = max(maxArea, area)
        return maxArea
    
    def explore_island(self, grid: List[List[int]], r: int, c: int) -> int:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        return 1 + self.explore_island(grid, r-1, c) + self.explore_island(grid, r+1, c) + self.explore_island(grid, r, c-1) + self.explore_island(grid, r, c+1)
            
