class Solution:
    def longestMountain(self, A: List[int]) -> int:
        longest = 0
        if len(A) < 2:
            return longest
        i = 1
        while i < len(A):
            start = i - 1
            
            # go up the mountain
            while i < len(A) and A[i] > A[i-1]:
                i += 1
                
            if start + 1 == i: #not valid mountain
                i += 1
                continue
                
            # peak of the mountain
            peak = i - 1
            
            #go down the mountain
            while i < len(A) and A[i] < A[i-1]:
                i += 1
                
            if peak + 1 == i: #not valid mountain
                i += 1
                continue
                
            longest = max(longest, i-start)
         
        return longest
