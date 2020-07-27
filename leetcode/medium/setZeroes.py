class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #locate 0's and save them in first row and first column
        m, n = len(matrix), len(matrix[0])
        firstRow, firstCol = False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # set row i to 0
                    matrix[0][j] = 0 # set column j to 0
                    firstRow = (True if i == 0 else firstRow)
                    firstCol = (True if j == 0 else firstCol)
        print(matrix)
        #first row and column indicates which rows/columns must be set to 0
        #set all rows to 0 (except the first one, it is used for columns)
        for row in range(1, m):
            if matrix[row][0] == 0:
                self.setRowToZero(matrix, row)
       
        #set all columns to 0
        for col in range(1, n):
            if matrix[0][col] == 0:
                self.setColToZero(matrix, col)
        
        #set the first row and col to 0 if needed
        if firstRow:
            self.setRowToZero(matrix, 0)
        if firstCol:
            self.setColToZero(matrix, 0)
    
    
    def setRowToZero(self, matrix: List[List[int]], row: int) -> None:
        for col in range(len(matrix[0])):
            matrix[row][col] = 0
    
    
    def setColToZero(self, matrix: List[List[int]], col: int) -> None:
        for row in range(len(matrix)):
            matrix[row][col] = 0
    
    
    
    
    
    
