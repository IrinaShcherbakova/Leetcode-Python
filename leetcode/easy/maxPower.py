class Solution:
    def maxPower(self, s: str) -> int:
        maxSeen = i = 0
        while i < len(s):
            start = i
            while i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
            if i - start + 1 > maxSeen:
                maxSeen = i - start + 1
            i += 1
        return maxSeen
    
