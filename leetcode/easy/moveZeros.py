class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = zero = 0
        while nonZero < len(nums):
            while nonZero < len(nums) and nums[nonZero] == 0:
                nonZero += 1
            if nonZero >= len(nums):
                return
            while zero < len(nums) and nums[zero] != 0:
                zero += 1
            if zero >= len(nums):
                return
            if zero > nonZero:
                nonZero += 1
                continue
            temp = nums[zero]
            nums[zero] = nums[nonZero]
            nums[nonZero] = temp
            nonZero += 1
