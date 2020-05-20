class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            freq = nums[i]
            val = nums[i+1]
            j = 0
            while j < freq:
                res.append(val)
                j += 1
            i += 2
        return res
