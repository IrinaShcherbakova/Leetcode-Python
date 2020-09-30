class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        max_int = len(nums)
        counts = [0] * max_int
        
        #
        for i, num in enumerate(nums):
            if num > max_int or num <= 0:
                continue
            else:
                counts[num-1] += 1
        
        for i, num in enumerate(counts):
            if num == 0:
                return i + 1
        return max_int+1
            
