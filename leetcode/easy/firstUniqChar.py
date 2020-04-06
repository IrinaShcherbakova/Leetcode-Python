class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = []
        seen = []
        for char in s:
            if char in seen:
                continue
            if char not in unique:
                unique.append(char)
            else:
                unique.remove(char)
                seen.append(char)
        
        return (-1 if len(unique) == 0 else s.index(unique[0]))
