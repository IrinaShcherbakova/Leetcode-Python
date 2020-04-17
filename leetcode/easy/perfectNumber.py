class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 2:
            return False
        divSum = 1
        limit = num ** 0.5
        i = 2
        while i <= limit:
            if num % i == 0:
                divSum = divSum + i + (num // i)
            i += 1
        return divSum == num
