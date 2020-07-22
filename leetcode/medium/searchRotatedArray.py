class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return (0 if nums[0] == target else -1)
        p = self.pivot(nums)
        if p == 0 or target <= nums[-1]:
            return self.binSearch(nums, target, p, len(nums)-1)
        return self.binSearch(nums, target, 0, p-1)

    
    def pivot(self, nums: List[int]) -> int:
        first, last = nums[0], nums[-1]
        if first < last:
            return 0
        if len(nums) == 2:
            return 1
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] >= first:
                low = mid+1
            elif nums[mid] < last:
                if mid-1 >= 0 and nums[mid-1] > nums[mid]:
                    return mid
                if mid+1 < len(nums) and nums[mid+1] < nums[mid]:
                    return mid
                high = mid-1
        return low
    
    def binSearch(self, nums: List[int], target: int, low: int, high: int) -> int:
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                return mid
        return (low if nums[low] == target else -1)
        
        
        
        
        
        
        
        
        
        
        
            
            
