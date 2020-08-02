class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = [] * len(nums)
        for i in range(len(nums)):
            memo.append([0,0])
        robFirst, dontRobFirst = self.robHouse(nums, 0, memo)
        return max(robFirst, dontRobFirst)
    
    #memo[i][0] - total money if we rob house i
    #memo[i][1] - total money if we don't rob house i
    def robHouse(self, nums: List[int], house: int, memo: List[int]) -> tuple:
        if house < len(memo) and (memo[house][0] > 0 or memo[house][1] > 0):
            return memo[house][0], memo[house][1]
        if house == len(nums) - 1:
            memo[house][0] = nums[house]
            memo[house][1] = 0
            return memo[house][0], memo[house][1]
        robNext, dontRobNext = self.robHouse(nums, house+1, memo)
        memo[house][0] = dontRobNext + nums[house]
        memo[house][1] = max(robNext, dontRobNext)
        return memo[house][0], memo[house][1]
       
