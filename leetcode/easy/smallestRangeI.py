class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxVal, minVal = A[0], A[0]
        for i in range(1, len(A)):
            if A[i] > maxVal:
                maxVal = A[i]
            if A[i] < minVal:
                minVal = A[i]
        if abs(maxVal - minVal) <= K*2:
            return 0
        return abs((maxVal - K) - (minVal + K))
