class Solution:
    # def findTheDifference(self, s: str, t: str) -> str:
    #     letters = {}
    #     for char in s:
    #         if char not in letters:
    #             letters[char] = 1
    #         else:
    #             letters.update({char: letters[char] + 1})
    #     for char in t:
    #         if char not in letters:
    #             return char
    #         value = letters[char]
    #         if value == 1:
    #             del letters[char]
    #         else:
    #             letters.update({char: value-1})
    
    def findTheDifference(self, s: str, t: str) -> str:  #runs faster then the first solution
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
