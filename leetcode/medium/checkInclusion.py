class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        substrings = set()
        N = len(s1)
        arr1 = self.counts(s1)
        
        #store all possible substrings of length N
        for i in range(len(s2)-N+1):
            substrings.add(s2[i:i+N])
        
        for substring in substrings:
            arr2 = self.counts(substring)
            if arr1 == arr2:
                return True      
        return False
            
        
    def counts(self, s: str) -> List[int]:
        arr = [0] * 26
        for char in s:
            index = ord(char) - 97
            arr[index] += 1
        return arr
    
            
