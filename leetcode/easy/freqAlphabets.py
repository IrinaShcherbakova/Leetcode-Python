class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if int(s[i]) != 1 and int(s[i]) != 2:
                res = res + chr(96+int(s[i]))
                i += 1
            else:
                if i+2 >= len(s):
                    res = res + chr(96+int(s[i]))
                    i += 1
                elif s[i+2] == '#':
                    number = s[i] + s[i+1]
                    print(number)
                    res = res + chr(96 + int(number))
                    i += 3
                else:
                    res = res + chr(96+int(s[i]))
                    i += 1
        return res
                
                             
                             
            
