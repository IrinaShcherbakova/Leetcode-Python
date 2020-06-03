class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                i += 1
                j -= 1
            elif A[i] % 2 != 0 and A[j] % 2 != 0: #both odd
                j -= 1
            elif A[i] % 2 == 0 and A[j] % 2 == 0: #both even
                i += 1
            else:
                i += 1
                j -= 1
        return A
