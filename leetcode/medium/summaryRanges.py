class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0:
            return res
        start = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1:
                cont_range = ((str(nums[start]) + "->" + str(nums[i-1])) if nums[start] < nums[i-1] else str(nums[start]))
                res.append(cont_range)
                start = i
        last_range = ((str(nums[start]) + "->" + str(nums[-1])) if nums[start] < nums[-1] else str(nums[start]))
        res.append(last_range)
        return res
