class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        maxNum = nums[0]
        maxIndex = 0
        for i in range(1, len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxIndex = i
        for i, num in enumerate(nums):
            if i != maxIndex and num*2 > maxNum:
                return -1
        return maxIndex
        
