class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1
