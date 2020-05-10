class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        nRows = len(A[0])
        result = []
        for i in range(nRows):
            newRow = []
            for row in A:
                newRow.append(row[i])
            result.append(newRow)
        return result



