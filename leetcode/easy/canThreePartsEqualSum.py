class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        totalSum = sum(A)
        if totalSum % 3 != 0:
            return False
        partition = totalSum // 3
        #locate first partition
        curSum = i = 0
        while i < len(A):
            curSum += A[i]
            i += 1
            if curSum == partition:
                break
        if i == len(A):
            return False
        
        #locate second partition
        curSum = 0
        while i < len(A):
            curSum += A[i]
            i += 1
            if curSum == partition:
                break
        if i == len(A):
            return False
        
        #locate third partition
        curSum = 0
        while i < len(A):
            curSum += A[i]
            i += 1
        return (True if curSum == partition else False)
