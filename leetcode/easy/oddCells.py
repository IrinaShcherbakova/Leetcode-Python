class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odd = 0
        matrix = [] 
        for i in range(n):
            row = [0] * m
            matrix.append(row)
        for pair in indices:
            ri = pair[0]
            ci = pair[1]
            #increment row ri in matrix
            print(matrix[ri])
            for i in range(m):
                matrix[ri][i] += 1
            #increment column ci in matrix:
            for i in range(n):
                matrix[i][ci] += 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 != 0:
                    odd += 1 
        return odd
