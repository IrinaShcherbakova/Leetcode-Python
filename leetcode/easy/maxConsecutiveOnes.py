class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = maxSeen = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                if current > maxSeen:
                    maxSeen = current
                current = 0
        return (maxSeen if maxSeen > current else current)
