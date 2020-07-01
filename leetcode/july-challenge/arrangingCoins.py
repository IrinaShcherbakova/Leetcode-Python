class Solution:
    def arrangeCoins(self, n: int) -> int:
        totalSum, k = 0, 1
        while totalSum < n:
            totalSum += k
            k += 1
        # print(totalSum)
        # print(k)
        if totalSum > n:
            return k - 2
        return k - 1
