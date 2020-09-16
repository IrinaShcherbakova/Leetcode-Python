class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = self.backspace_string(S)
        s2 = self.backspace_string(T)
        if len(s1) != len(s2):
            return False
        return s1 == s2
        
        
        
    def backspace_string(self, s: str) -> str:
        i = len(s) - 1
        backspaces = 0
        res = []
        while i >= 0:
            if s[i] == '#':
                backspaces += 1
            elif backspaces:
                backspaces -= 1
            else:
                res.append(s[i])
            i -= 1
        res = res[::-1]
        return "".join(res)
