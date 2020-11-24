class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                cur = min(rowSum[i], colSum[j])
                row.append(cur)
                rowSum[i] -= cur
                colSum[j] -= cur
            matrix.append(row)
        return matrix
            
