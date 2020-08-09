class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh, minutes = 0, 0
        # print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return minutes
        
        while rotten:
            new_rotten_count, rotten = self.rot(grid, rotten)
            # print("after round: %s" %grid)
            fresh -= new_rotten_count
            minutes += 1
            if fresh == 0:
                return minutes
            
        return (-1 if fresh > 0 else minutes)
    
    
    def rot(self, grid: List[List[int]], rotten: List[List[int]]) -> tuple:
        new_rotten_count = 0
        new_rotten_coord = []
        for location in rotten:
            row, col = location[0], location[1]
            new_rotten_count += self.expand(grid, row, col, new_rotten_coord)
        return new_rotten_count, new_rotten_coord
    
    
    # check up, down, left and right
    def expand(self, grid: List[List[int]], row: int, col: int, res: List[List[int]]) -> int:
        new_rotten = 0
        # check up
        if row - 1 >= 0 and grid[row-1][col] == 1:
            grid[row-1][col] = 2
            new_rotten += 1
            res.append([row-1,col])
        
        #check down
        if row + 1 < len(grid) and grid[row+1][col] == 1:
            grid[row+1][col] = 2
            new_rotten += 1
            res.append([row+1,col])
            
        # check left
        if col - 1 >= 0 and grid[row][col-1] == 1:
            grid[row][col-1] = 2
            new_rotten += 1
            res.append([row,col-1])
        
        # check right
        if col + 1 < len(grid[0]) and grid[row][col+1] == 1:
            grid[row][col+1] = 2
            new_rotten += 1
            res.append([row,col+1])
            
        return new_rotten
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
