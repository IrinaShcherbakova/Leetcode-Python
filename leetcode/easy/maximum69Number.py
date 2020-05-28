class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ""
        numStr = str(num)
        i = 0
        while i < len(numStr) and numStr[i] == '9':
            res += '9'
            i += 1
        if i == len(numStr):
            return int(res)
        res += '9' 
        return res + numStr[i+1:len(numStr)]
