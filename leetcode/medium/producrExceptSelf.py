class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums)
        after = [1] * len(nums)
        
        #calculate products of all numbers before nums[i]
        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]
        
        #calculate products of all numbers after nums[i] 
        for i in range(len(nums)-2, -1, -1):
            after[i] = after[i+1] * nums[i+1]
        
        #multiply after[i] and before[i]
        for i in range(len(before)):
            before[i] *= after[i]
         
        return before
