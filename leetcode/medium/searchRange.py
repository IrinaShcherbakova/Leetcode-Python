class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return self.findRange(nums, mid)
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1,-1] if len(nums) == 0 or nums[low] != target else self.findRange(nums, low)
    
    def findRange(self, nums: List[int], index: int) -> List[int]:
        i, j = index, index
        #locate lower bound
        while i-1 >= 0 and nums[i-1] == nums[i]:
            i -= 1
        #locate upper bound
        while j+1 < len(nums) and nums[j+1] == nums[j]:
            j += 1
        return [i, j]
        
        
        
