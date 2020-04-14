class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in s:
            while i < len(t) and t[i] != char:
                i += 1
            if i >= len(t):
                return False
            i += 1
        return True
                
