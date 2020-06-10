class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        shorter = (nums1 if len(nums1) < len(nums2) else nums2)
        longer = (nums1 if len(nums1) >= len(nums2) else nums2)
        res = []
        pool = set()
        seen = set()
        for num in longer:
            if num not in pool:
                pool.add(num)
        for num in shorter:
            if num in seen:
                continue
            else:
                seen.add(num)
                if num in pool:
                    res.append(num)
        return res
            
        
