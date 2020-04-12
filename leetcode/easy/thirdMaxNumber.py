class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        prevMax = globalMax = nums[-1]
        counter = 1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < prevMax:
                counter += 1
                if counter == 3:
                    return nums[i]
                prevMax = nums[i]
            i -= 1
        return globalMax
        
