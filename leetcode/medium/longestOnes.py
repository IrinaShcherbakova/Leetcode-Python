class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zero_info = self.form_zero_info(A)
        if not zero_info:
            return len(A)
        if K == 0:
            return self.max_subsequence(zero_info)
        
        start, end = 0, 1
        longest = 0
        current = zero_info[start][0] + zero_info[start][1] + 1     
        # place j at the end of K subsequence
        while end < len(zero_info) and end < K:
            current = current + zero_info[end][1] + 1
            end += 1
        longest = max(longest, current)
        
        # move end and start one step forward
        while end < len(zero_info):
            current = current - zero_info[start][0] - 1
            current = current + zero_info[end][1] + 1
            start += 1
            end += 1
            longest = max(longest, current)
        return longest              
   
                         
    def form_zero_info(self, A: List[int]) -> List[List[int]]:
        zero_info = []  # contains # of 1's to the left and to the right       
        ones, i = 0, 0
        while i < len(A):
            if A[i] == 1:
                ones += 1
                i += 1
            else:   # new zero group starts at index i
                if zero_info:
                    zero_info[-1][1] = ones        
                zero_info.append([ones, 0])               
                j = i + 1  # skip consecutive zero's
                while j < len(A) and A[j] == 0:
                    zero_info.append([0,0])
                    j += 1
                i = j
                ones = 0    
        # set the right count of last zero to ones
        if zero_info:
            zero_info[-1][1] = ones    
        return zero_info
                
      
    def max_subsequence(self, zero_info: List[List[int]]) -> int:
        longest = 0
        for info in zero_info:
            longest = max(longest, info[0], info[1])
        return longest
        
            
            
            
