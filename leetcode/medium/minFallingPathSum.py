class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if len(A) == 1:
            return min(A[0])
        rowMin = 0
        for i in range(len(A) - 2, -1, -1):
            rowMin = A[i+1][0] + A[i][0]
            for j in range(len(A[0])):
                path = self.getMinPath(A, i, j)
                rowMin = min(rowMin, path)
                A[i][j] = path
        return rowMin
                
                
    def getMinPath(self, A: List[List[int]], r: int, c: int) -> int:
        adjacent = [A[r+1][c]]
        if c - 1 >= 0:
            adjacent.append(A[r+1][c-1])
        if c + 1 < len(A[0]):
            adjacent.append(A[r+1][c+1])
        return A[r][c] + min(adjacent)
