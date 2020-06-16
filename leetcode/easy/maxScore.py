class Solution:
    def maxScore(self, s: str) -> int:
        zeros = [None] * len(s)
        ones = [None] * len(s)
        
        #count zero scores
        zeroCounter = 0
        for i, char in enumerate(s):
            if char == '0':
                zeroCounter += 1
            zeros[i] = zeroCounter 
        
        #count one scores
        oneCounter = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                oneCounter += 1
            ones[i] = oneCounter 
        
        #find max possible score
        maxScore = 0
        for i in range(1, len(s)):
            maxScore = max(maxScore, zeros[i-1] + ones[i])
        return maxScore
                
