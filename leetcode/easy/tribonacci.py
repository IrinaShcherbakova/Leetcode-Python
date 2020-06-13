class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        first = 0
        second = 1
        third = 1
        cur = None
        for i in range(3, n+1):
            cur = first + second + third
            first = second
            second = third
            third = cur
        return cur
