
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [None] * len(nums)
        for i in range(len(nums)):
            #print(nums[i])
            if target[index[i]] == None:
                target[index[i]] = nums[i]
                #print(target)
            else:
                temp = target[index[i]]
                target[index[i]] = nums[i]
                j = index[i] + 1
                while j < len(target) and target[j] != None:
                    nextNum = target[j]
                    target[j] = temp
                    temp = nextNum
                    j += 1
                target[j] = temp
                #print(target)
        return target
