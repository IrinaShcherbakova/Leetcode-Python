class Solution:
    def findMin(self, nums: List[int]) -> int:
        first, last = nums[0], nums[-1]
        if first < last: #array is not rotated
            return first
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] >= first:
                left = mid + 1
            elif nums[mid] <= last:
                right = mid
        return nums[left]
