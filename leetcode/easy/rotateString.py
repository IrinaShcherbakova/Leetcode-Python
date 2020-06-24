class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        AA = A + A
        i = 0
        while i < len(A):
            if AA[i] == B[0] and self.isSubstring(AA[i:len(AA)], B):
                #check if B is a substring of AA
                return True
            i += 1
        return (True if len(A) == 0 else False)
                
                           
    def isSubstring(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                return False
        return True
        
