class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        rob_last, skip_last = [0] * len(nums), [0] * len(nums)
           
        rob_last[-1] = nums[-1]
        rob_last[-2] = max(nums[-2], rob_last[-1])
        
        skip_last[-2] = nums[-2]
        
        for i in range(len(nums)-3, 0,-1):
            rob_last[i] = max(rob_last[i+2] + nums[i], rob_last[i+1])
            skip_last[i] = max(skip_last[i+2] + nums[i], skip_last[i+1])
        
        rob_last[0] = rob_last[1]
        skip_last[0] = max(skip_last[2] + nums[0], skip_last[1])
        return max(rob_last[0], skip_last[0])
