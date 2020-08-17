class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        flip_states = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.change_state(board, i, j):
                    flip_states.append([i,j])
        for state in flip_states:
            row, col = state[0], state[1]
            board[row][col] = (0 if board[row][col] == 1 else 1)
        return
    
    
    def change_state(self, board: List[List[int]], row: int, col: int) -> bool:
        # for loop checks all 8 neighbors and the cell itself. That's why we substract the value of the cell in the beginning if it is a live cell
        live_neighbors = (0 if board[row][col] == 0 else -1)
        dr, dc = -1, -1
        for i in range(dr, 2, 1):
            for j in range(dc, 2, 1):
                if row+i < 0 or row+i >= len(board) or col+j < 0 or col+j >= len(board[0]) or board[row+i][col+j] == 0:
                    continue
                else:
                    live_neighbors += 1
        if board[row][col] == 1 and live_neighbors < 2:
            return True
        if board[row][col] == 1 and live_neighbors > 3:
            return True
        if board[row][col] == 0 and live_neighbors == 3:
            return True
        return False
        
        
        
        
        
                    
                    
                    
                    
                    
                    
                
            
