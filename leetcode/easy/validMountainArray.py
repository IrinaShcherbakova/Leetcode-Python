class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        #find a peak element
        peak = None
        # go up
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                return False
            if A[i] < A[i-1]:
                peak = i-1
                break
        if not peak or peak == len(A) - 1:
            return False
        # go down
        for i in range(peak+1, len(A)):
            if A[i] >= A[i-1]:
                return False
        return True
