class Solution:
    def countSegments(self, s: str) -> int:
        count, i = 0, 0
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                return count
            while i < len(s) and s[i] != ' ':
                i += 1
            count += 1
        return count
