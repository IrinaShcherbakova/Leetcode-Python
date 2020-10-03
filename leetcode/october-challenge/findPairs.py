class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        unique_nums = set(nums)
        pairs = 0
        for num in unique_nums:
            target = num - k
            if target in counts:
                if target == num and counts[target] > 1:
                    pairs += 1
                elif target != num:
                    pairs += 1
        return pairs
