class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        i = 3
        while i < n:
            c = a+b
            a = b
            b = c
            i += 1
        return a+b
