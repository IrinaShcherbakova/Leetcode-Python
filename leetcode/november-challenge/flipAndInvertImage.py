class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rows, cols = len(A), len(A[0])
        cols_mid = len(A[0])//2 if len(A[0])%2 == 0 else len(A[0])//2+1
        for i in range(rows):
            for j in range(cols_mid):
                first = 0 if A[i][j] == 1 else 1 
                last = 0 if A[i][cols-1-j] == 1 else 1
                A[i][j] = last
                A[i][cols-1-j] = first
        return A
