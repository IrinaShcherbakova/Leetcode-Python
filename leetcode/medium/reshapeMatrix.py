class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        
        if r * c != rows * cols:
            return mat
        
        res = []
        cur_row, cur_col = 0, 0
        
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(mat[cur_row][cur_col])
                cur_col = 0 if cur_col + 1 == cols else cur_col + 1
                if cur_col == 0:
                    cur_row += 1
            res.append(new_row)
            
        return res
                
