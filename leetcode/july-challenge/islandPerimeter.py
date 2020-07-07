class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    #edge cases horizontally
                    if j == 0:
                        perimeter += 1
                    if j == len(grid[i]) - 1:
                        perimeter += 1
                    if j - 1 >= 0 and grid[i][j-1] == 0:
                        perimeter += 1
                    if j + 1 < len(grid[i]) and grid[i][j+1] == 0:
                        perimeter += 1
                    #edge cases vertically
                    if i == 0:
                        perimeter += 1
                    if i == len(grid) - 1:
                        perimeter += 1
                    if i - 1 >= 0 and grid[i-1][j] == 0:
                        perimeter += 1
                    if i + 1 < len(grid) and grid[i+1][j] == 0:
                        perimeter += 1
        return perimeter
                    
                    
                    
