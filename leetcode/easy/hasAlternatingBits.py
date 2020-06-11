class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n > 0:
            cur = n % 2
            if prev == cur:
                return False
            prev = cur
            n = n // 2
        return True
