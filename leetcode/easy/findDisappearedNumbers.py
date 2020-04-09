class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if nums is None:
            return None
        nums.sort()
        i = 1
        j = 0
        res = []
        while j < len(nums):
            if nums[j] != i:
                res.append(i)
                i += 1
                continue
            if nums[j] == i:
                if j+1 < len(nums) and nums[j+1] != i:
                    i += 1
            j += 1
        while i < len(nums):
            i += 1
            res.append(i)
        return res                
            
