class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0
        j = 1
        while i < len(A) and j < len(A):
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                
            if A[i] % 2 == 0:   i += 2
            if A[j] % 2 != 0:   j += 2
        return A
            
