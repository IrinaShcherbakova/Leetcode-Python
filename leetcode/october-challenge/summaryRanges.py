class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if i - 1 == start: # range consists of one number
                    res.append(str(nums[start]))
                else:
                    cur_range = str(nums[start]) + "->" + str(nums[i-1]) 
                    res.append(cur_range)
                start = i
        if start == len(nums) - 1:
            res.append(str(nums[start]))
        else:
            cur_range = str(nums[start]) + "->" + str(nums[-1]) 
            res.append(cur_range)
        return res
                     
