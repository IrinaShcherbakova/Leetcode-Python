class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0] if nums[0] < nums[-1] else nums[-1]
    
            
            
