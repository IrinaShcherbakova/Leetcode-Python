class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) == 0:
            return []
        mapping = [None] * (max(nums2) + 1)
        for i in range(len(nums2)):
            mapping[nums2[i]] = i
        res = []
        for num in nums1:
            pos = mapping[num] + 1
            while pos < len(nums2):
                if nums2[pos] > num:
                    res.append(nums2[pos])
                    break
                pos += 1
            if pos == len(nums2):
                res.append(-1)
        return res
        
            
