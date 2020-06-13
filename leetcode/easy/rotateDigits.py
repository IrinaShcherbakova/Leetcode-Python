class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for num in range(2, N+1):
            if self.isGood(num):
                count += 1
        return count
    
      
    def isGood(self, num: int) -> bool:
        #print(num)
        good = {2 : 5, 5 : 2, 6 : 9, 9 : 6, 0 : 0, 1 : 1, 8 : 8}
        bad = {3, 4, 7}
        newNum = 0
        oldNum = num
        count = 1
        while num > 0:
            rem = num % 10
            #print(rem)
            if rem in bad:
                return False
            newNum = newNum + (good[rem]) * count
            count *= 10
            num = num // 10
        return newNum != oldNum
