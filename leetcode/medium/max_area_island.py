class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.visit_island(row, col, grid))
        return max_area
    
    
    def visit_island(self, row:int, col: int, grid: List[List[int]]) -> int:
        if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
            return 0
        if grid[row][col] == 0:
            return 0
        if grid[row][col] == -1:
            return 0
        grid[row][col] = -1 # visit island
        return 1 + self.visit_island(row+1, col, grid) + self.visit_island(row-1, col, grid) + self.visit_island(row, col+1, grid) + self.visit_island(row, col-1, grid)
        
