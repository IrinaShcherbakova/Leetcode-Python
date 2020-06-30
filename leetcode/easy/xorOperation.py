class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        prev = start
        for i in range(1, n):
            cur = start + 2*i
            prev = prev ^ cur
        return prev
