class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        if len(a) > len(b):
            b = self.padZeros(b, len(a)-len(b))
        else:
            a = self.padZeros(a, len(b)-len(a))
        for i in range(len(a)-1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                if carry >= 1:
                    res = '1' + res
                else:
                    carry += 1
                    res = '0' + res
            elif a[i] == '0' and b[i] == '0':
                if carry >= 1:
                    res = '1' + res
                    carry -= 1
                else:
                    res = '0' + res
            elif a[i] == '1' or b[i] == '1':
                if carry >= 1:
                    res = '0' + res
                else:
                    res = '1' + res
        for i in range(carry):
            res = '1' + res
        return res
    
    
    def padZeros(self, s: str, num: int) -> str:
        return ('0' * num) + s
        
        
        
