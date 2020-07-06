class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        res.append((digits[-1] + 1) % 10)
        carry = (digits[-1] + 1) // 10
        # print("carry is %s" %carry)
        for i in range(len(digits)-2,-1,-1):
            res.append((digits[i] + carry) % 10)
            carry = (digits[i] + carry) // 10
        if carry == 1:
            res.append(1)
        # print(digits)
        return res[::-1]
            
