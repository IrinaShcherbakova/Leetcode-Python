class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binSearch(nums, 0, len(nums))
    
    def binSearch(self, nums: List[int], start: int, end: int) -> int:
        if start >= end:
            return -1
        mid = start + (end-start) // 2
        if mid - 1 < 0 and mid + 1 >= len(nums):
            return mid
        if mid - 1 < 0 and nums[mid] > nums[mid+1]:
            return mid
        if mid + 1 >= len(nums) and nums[mid] > nums[mid-1]:
            return mid
        if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
            return mid
        left = self.binSearch(nums, start, mid)
        if left >= 0:
            return left
        return self.binSearch(nums, mid+1, end)
