class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        count = 0
        for num in sorted(counts, key=counts.get, reverse=True):
            res.append(num)
            count += 1
            if count == k:
                return res
        return res
                
