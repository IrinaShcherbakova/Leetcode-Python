# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low < high:
            middle = (high+low)// 2
            res = guess(middle)
            if res == 0:
                return middle
            if res == -1:
                high = middle
                continue
            if low == middle:
                low += 1
            else:
                low = middle
        return low
