class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = nums[0]
        second = nums[1]
        if first < second:
            first = second
            second = nums[0]
        for i in range(2, len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return (first-1)*(second-1)
