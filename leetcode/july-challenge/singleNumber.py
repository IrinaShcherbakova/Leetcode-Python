class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = set()
        for num in nums:
            if num in counts:
                counts.discard(num)
            else:
                counts.add(num)
        res = []
        for num in counts:
            res.append(num)
        return res
        
