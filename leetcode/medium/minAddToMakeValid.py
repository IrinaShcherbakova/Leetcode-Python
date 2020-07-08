class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        openPar, res = 0, 0
        for char in S:
            if char == '(':
                openPar += 1
            elif char == ')':
                if openPar <= 0:
                    res += 1
                else:
                    openPar -= 1
        return res + openPar
