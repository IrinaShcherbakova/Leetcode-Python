class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        count = 0
        for i  in range(rows, -1, -1):
            for j in range(cols, -1, -1):
                if grid[i][j] >= 0:
                    break
                count += 1
        return count
