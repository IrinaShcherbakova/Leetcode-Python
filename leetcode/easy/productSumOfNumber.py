class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumDigits = 0
        productDigits = 1
        for digit in str(n):
            sumDigits += int(digit)
            productDigits *= int(digit)
        return productDigits-sumDigits
