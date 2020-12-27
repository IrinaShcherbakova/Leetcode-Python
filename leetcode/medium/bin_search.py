class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        return self.recurse_search(nums, 0, len(nums)-1, target)
    
    
    def recurse_search(self, nums: List[int], l: int, r: int, target: int) -> bool: 
    
        if l > r:
            return False
        
        mid = l + (r-l)//2
        if nums[mid] == target:
            return True
        
        if nums[mid] > target and nums[l] <= target:
            return self.recurse_search(nums, l, mid-1, target)
        
        if nums[mid] > target and nums[l] > target and nums[mid] > nums[l]:
            return self.recurse_search(nums, mid+1, r, target)
        
        if nums[mid] < target and nums[r] >= target:
            return self.recurse_search(nums, mid+1, r, target)
        
        if nums[mid] > target and nums[r] < target:
            return self.recurse_search(nums, l, mid-1, target)
        
        return self.recurse_search(nums, l, mid-1, target) or self.recurse_search(nums, mid+1, r, target)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
