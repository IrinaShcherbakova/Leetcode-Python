class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = [0] * (n + 1)
        i = 1
        while i <= n:
            sumDigits = self.sumOfDigits(i)
            #print("sum digits of %s is %s " %(i, sumDigits))
            counts[sumDigits] += 1
            i += 1
        maxSize = max(counts)
        ans = 0
        for count in counts:
            if count == maxSize:
                ans += 1
        return ans
    
    
    def sumOfDigits(self, n: int) -> int:
        if n < 10:
            return n
        res = 0
        while n > 0:
            res = res + n % 10
            n = n // 10
        return res
