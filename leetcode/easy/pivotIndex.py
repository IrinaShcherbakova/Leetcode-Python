class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        indexSum = []
        curSum = 0
        for num in nums:
            curSum += num
            indexSum.append(curSum)
        if indexSum[-1] - indexSum[0] == 0:
            return 0        
        for i in range(1, len(nums)-1):
            if indexSum[i-1] == indexSum[-1] - indexSum[i]:
                return i
        if indexSum[-2] == 0:
            return len(nums) - 1  
        return -1
