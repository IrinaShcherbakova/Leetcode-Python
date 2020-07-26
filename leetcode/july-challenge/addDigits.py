class Solution:
#     def addDigits(self, num: int) -> int:
#         while len(str(num)) > 1:
#             num = self.addDigitsHelper(num)
#         return num
    
#     def addDigitsHelper(self, num: int) -> int:
#         res = 0
#         for ch in str(num):
#             res += int(ch)
#         return res

    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + ((num - 1) % 9)
        
