class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        numA = 0
        multip = 1
        for i in range(len(A) - 1, -1, -1):
            numA = A[i] * multip + numA
            multip *= 10
        newA = numA + K
        lenA = len(str(newA))
        res = [0]*lenA
        i = lenA - 1
        while newA > 0:
            res[i] = newA % 10
            newA = newA // 10
            i -= 1
        return res
