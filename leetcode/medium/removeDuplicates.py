class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        write = 0
        left, right = 0, 1 
        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
                continue
            nums[write] = nums[left]
            write += 1
            if right - left > 1:
                nums[write] = nums[left]
                write += 1
            left = right
            right = left + 1
        
        nums[write] = nums[left]
        if right - left > 1:
            write += 1
            nums[write] = nums[left]
        return write + 1
                
            
        
