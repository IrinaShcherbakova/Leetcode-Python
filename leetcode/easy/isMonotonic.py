class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return True
        i = 1
        while i < len(A) and A[i] == A[i-1]:
            i += 1
        if i == len(A):
            return True
        if A[i-1] < A[i]:
            return self.isIncreasing(A)
        return self.isDecreasing(A)
        
    
    def isIncreasing(self, A: List[int]) -> bool:
        prev = A[0]
        for num in A:
            if num >= prev:
                prev = num
            else:
                return False
        return True
    
    
    def isDecreasing(self, A: List[int]) -> bool:
        print(A)
        prev = A[0]
        for num in A:
            if num <= prev:
                prev = num
            else:
                return False
        return True
