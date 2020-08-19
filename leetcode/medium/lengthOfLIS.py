class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        increase_counts = [0] * len(nums)
        increase_counts[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i] and increase_counts[j] > increase_counts[i]:
                    increase_counts[i] = increase_counts[j]
            increase_counts[i] += 1
            longest = max(longest, increase_counts[i])
        return longest
    
    
   
        
        
        
        
