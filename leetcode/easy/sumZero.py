class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        res = [None]*n
        negIndex = posIndex = 0
        posSum = 0
        if n % 2 == 0:
            posIndex = (n//2)-1
        else:
            posIndex = n//2
        index = 1
        for i in range(posIndex, len(res)):
            res[i] = index
            posSum += index
            index+=1
        negSum = 0
        for i in range(0, posIndex-1):
            res[i] = (i+1)*-1
            negSum -= (i+1)
        res[posIndex-1] = -1*(negSum+posSum)
        return res
