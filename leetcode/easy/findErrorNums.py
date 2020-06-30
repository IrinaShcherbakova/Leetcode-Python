class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = [0] * (len(nums)+1)
        missing, dupl = 0, 0
        for num in nums:
            counts[num] += 1
            if counts[num] == 2:
                dupl = num
        #print(counts)
        for i in range(1, len(counts)):
            if counts[i] == 0:
                missing = i
        return [dupl, missing]
