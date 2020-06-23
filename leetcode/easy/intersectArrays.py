class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        shorter, longer = None, None
        if len(nums1) < len(nums2):
            shorter = nums1
            longer = nums2
        else:
            shorter = nums2
            longer = nums1
        counts = {}
        for num in shorter:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
        res = []
        for num in longer:
            if num in counts:
                res.append(num)
                if counts[num] == 1:
                    counts.pop(num)
                else:
                    counts[num] = counts[num] - 1
        return res
        
