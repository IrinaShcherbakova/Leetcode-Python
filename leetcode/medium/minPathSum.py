class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        minPathAtCell = []
        for i in range(len(grid)):
            minPathAtCell.append([-1]*len(grid[0]))
        return self.getMinPath(grid, minPathAtCell, 0, 0)
        
        
    def getMinPath(self, grid: List[List[int]], minPathAtCell: List[List[int]], r: int, c: int) -> int:
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
            return -1
        if minPathAtCell[r][c] >= 0:
            return minPathAtCell[r][c]
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            minPathAtCell[r][c] = grid[r][c]
            return minPathAtCell[r][c]
        right = self.getMinPath(grid, minPathAtCell, r, c+1)
        down = self.getMinPath(grid, minPathAtCell, r+1, c)
        if right < 0 or down < 0:
            minPathAtCell[r][c] = grid[r][c] + (right if right >= 0 else down)
        else:
            minPathAtCell[r][c] = grid[r][c] + min(right, down)
        return minPathAtCell[r][c]
    
        
