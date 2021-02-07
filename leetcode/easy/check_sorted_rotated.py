class Solution:
    def check(self, nums: List[int]) -> bool:
        rotate_point = -1
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                rotate_point = i
                break
        
        if rotate_point < 0:
            return True
        
        cur = rotate_point + 1;
        prev = nums[rotate_point]
        while cur != rotate_point:
            if cur >= len(nums):
                cur = 0
            elif nums[cur] < prev:
                return False
            else:
                prev = nums[cur]
                cur += 1
            
        return True
