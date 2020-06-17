class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = []
        for i in range(3):
            grid.append([None,None,None])
        
        filledCells = 0
        for i, move in enumerate(moves):
            row = move[0]
            col = move[1]
            if i % 2 == 0:
                grid[row][col] = 'X'
            else:
                grid[row][col] = 'O'
            filledCells += 1
        
        for row in grid:
            print(row)
        
        #check rows
        for row in grid:
            if row[0] == row[1] == row[2] and row[0] != None:
                return ('A' if row[0] == 'X' else 'B')
            
        #check columns
        for i in range(3):
            if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != None:
                return ('A' if grid[0][i] == 'X' else 'B')
            
        #check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != None:
            return ('A' if grid[0][0] == 'X' else 'B')
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != None:
            return ('A' if grid[0][2] == 'X' else 'B')
        
        print(filledCells)
        return ("Draw" if filledCells == 9 else "Pending")
        
