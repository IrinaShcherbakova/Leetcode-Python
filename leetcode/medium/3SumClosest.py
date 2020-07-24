class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(1, len(nums)-1):
            start, end, neededSum = i, len(nums)-1, target - nums[i-1]
            while start < end:
                twoSum = nums[start] + nums[end]
                if abs(neededSum - twoSum) < abs(target - res):
                    res = nums[i-1] + twoSum
                if neededSum > twoSum:
                    start += 1
                elif neededSum < twoSum:
                    end -= 1
                else:
                    return target
        return res

                
            
                
        
