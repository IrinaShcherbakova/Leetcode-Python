class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += self.can_communicate(grid, i, j)
        return total
                    
                                   
    def can_communicate(self, grid: List[List[int]], row: int, col: int) -> int:
        # mark current server as visited (2)
        grid[row][col] = 2
        
        # scan corresponding row in the right direction
        for j in range(col+1, len(grid[0])):
            if grid[row][j] == 1:
                # found another not visted server on the same row. Mark it as visited and return 2
                grid[row][j] = 2
                return 2
            if grid[row][j] == 2: 
                return 1
            
        # scan corresponding row in the left direction
        for j in range(0, col):
            if grid[row][j] == 1:
                grid[row][j] = 2
                return 2
            if grid[row][j] == 2: 
                return 1
            
        # scan corresponding column in the bottom direction
        for i in range(row+1, len(grid)):
            if grid[i][col] == 1:
                grid[i][col] = 2
                return 2
            if grid[i][col] == 2: 
                return 1
        
        # scan corresponding column in the top direction
        for i in range(0, row):
            if grid[i][col] == 1:
                grid[i][col] = 2
                return 2
            if grid[i][col] == 2: 
                return 1
            
        # no service found on the same row and column, return 0
        return 0
        
            
        
            
            
            
            
            
            
            
            
            
        
