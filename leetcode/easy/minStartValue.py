class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prev_sum = 0
        min_sum = nums[0]
        for i, num in enumerate(nums):
            prev_sum = prev_sum + num
            min_sum = min(min_sum, prev_sum)
        if min_sum > 0:
            return 1
        return abs(min_sum)+1
