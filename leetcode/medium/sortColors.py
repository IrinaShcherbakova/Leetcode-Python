class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        index = 0
        for color, count in enumerate(counts):
            for i in range(count):
                nums[index] = color
                index += 1
        return
