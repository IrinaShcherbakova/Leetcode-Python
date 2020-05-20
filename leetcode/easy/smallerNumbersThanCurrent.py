
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = nums.copy()
        sortedNums.sort()
        res = []
        for num in nums:
            value = sortedNums.index(num)
            res.append(value)
        return res

