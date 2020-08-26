class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        border = []
        self.expand_component(grid, r0, c0, grid[r0][c0], border)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    grid[i][j] *= -1  
        for cell in border:
            r, c = cell[0], cell[1]
            grid[r][c] = color
        return grid
     
    
    def expand_component(self, grid: List[List[int]], r: int, c: int, old_color: int, border: List[List[int]]) -> None:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 
        
        # mark visited cells as negative
        if grid[r][c] < 0:
            return
        
        if grid[r][c] != old_color:
            grid[r][c] *= -1
            return
        
        # check if we deal with isolated component
        if self.adjacent_to_other_color(grid, r, c):
            border.append([r,c])        
        
        # check if we deal with a square at the boundary
        elif self.on_boundary_of_grid(grid, r, c):
            border.append([r,c])
        
        grid[r][c] *= -1
        
        self.expand_component(grid, r-1, c, old_color, border)
        self.expand_component(grid, r+1, c, old_color, border)
        self.expand_component(grid, r, c+1, old_color, border)
        self.expand_component(grid, r, c-1, old_color, border)
        return
    
    
    def on_boundary_of_grid(self, grid: List[List[int]], r: int, c: int) -> bool:
        if r - 1 < 0 or r + 1 >= len(grid) or c - 1 < 0 or c + 1 >= len(grid[0]):
            return True
        return False
    
    
    def adjacent_to_other_color(self, grid: List[List[int]], r: int, c: int) -> bool:
        cell_color = grid[r][c]
        if r - 1 >= 0 and abs(grid[r-1][c]) != cell_color:
            return True
        if r + 1 < len(grid) and abs(grid[r+1][c]) != cell_color:
            return True
        if c - 1 >= 0 and abs(grid[r][c-1]) != cell_color:
            return True
        if c + 1 < len(grid[0]) and abs(grid[r][c+1]) != cell_color:
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
            
        
    
    
    
