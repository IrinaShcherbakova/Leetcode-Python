class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num
        while left <= right:
            middle = left + (right-left) // 2
            if middle*middle == num:
                return True
            elif middle*middle > num:
                right = middle - 1
            else: 
                left = middle + 1
        return False
