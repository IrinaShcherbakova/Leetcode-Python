class Solution:
    def hammingWeight(self, n: int) -> int:
        #print(bin(n))
        count = 0
        num = str(bin(n))
        print(num)
        for digit in num:
            if digit == '1':
                count += 1
        return count
