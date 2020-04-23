class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        middle = (high - low) // 2
        while low <= high:
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                high = middle - 1
                middle = (high - low) // 2
            else:
                low = middle + 1
                middle = high - (high - low)//2
        return -1
