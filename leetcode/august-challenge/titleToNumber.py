class Solution:
    def titleToNumber(self, s: str) -> int:
        totalLetters = 26
        power = len(s) - 1
        res = 0
        #print(power)
        for i in range(len(s) - 1):
            charOrder = ord(s[i]) - 64
            #print(charOrder)
            res = res + charOrder*(totalLetters**power)
            power -= 1
        res = res + (ord(s[-1]) - 64)
        return res
            
