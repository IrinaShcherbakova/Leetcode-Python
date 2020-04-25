class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        childPtr = cookiesPtr = count = 0
        while childPtr < len(g):
            while cookiesPtr < len(s) and g[childPtr] > s[cookiesPtr]:
                cookiesPtr += 1
            if cookiesPtr >= len(s):
                return count
            count += 1
            childPtr += 1
            cookiesPtr += 1
        return count
        
