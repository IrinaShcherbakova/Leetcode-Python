class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        min_steps_needed = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < min_steps_needed:
                min_steps_needed += 1
            else:
                min_steps_needed = 1
        return nums[0] >= min_steps_needed
            
        
        
