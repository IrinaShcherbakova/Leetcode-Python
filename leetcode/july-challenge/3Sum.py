class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            # print(target)
            low, high = i+1, len(nums)-1
            while low < high:
                if nums[low] + nums[high] > target:
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1       
                elif nums[low] + nums[high] == target:
                    # print("low, high is %s %s" %(nums[low], nums[high]))
                    res.append([nums[i],nums[low],nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    while high > low and nums[high] == nums[high+1]:
                        high -= 1
        return res
                

    #returns index of found element,otherwise -1
    def binSearch(self, nums: List[int], low: int, target: int) -> int:  
        high = len(nums) - 1
        while low <= high:
            middle = low + (high-low) // 2
            if target < nums[middle]:
                high = middle - 1
            elif target > nums[middle]:
                low = middle + 1
            else:
                return middle
        return -1
