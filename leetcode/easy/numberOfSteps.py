class Solution:
    def numberOfSteps (self, num: int) -> int:
        counter = 0
        while num > 0:
            counter += 1
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
        return counter
