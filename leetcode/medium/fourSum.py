class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                low, high = j+1, len(nums)-1
                while low < high:
                    cur = nums[i]+nums[j]+nums[low]+nums[high]
                    if cur == target:
                        res.append([nums[i],nums[j],nums[low],nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low-1]:
                            low += 1
                        while high > low and nums[high+1] == nums[high]:
                            high -= 1
                    elif cur < target:
                        low += 1
                    else:
                        high -= 1
        return res
