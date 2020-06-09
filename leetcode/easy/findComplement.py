class Solution:
    def findComplement(self, num: int) -> int:
        power = 0
        res = 0
        while num > 0:
            bit = (0 if num%2 == 1 else 1)
            res = res + (bit*2**power)
            power += 1
            num = num // 2
        return res                                                  
                                                                         
