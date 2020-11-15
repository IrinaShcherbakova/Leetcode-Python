class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_arr = [0] * 26
        s_arr = [0] * 26
        res = []
        
        for char in p:
            self.change_count(p_arr, char, 1)
            
        for i in range(len(s)-1, len(s)-len(p)-1, -1):
            self.change_count(s_arr, s[i], 1)
        
        if p_arr == s_arr:
                res.append(i)
        
        for i in range(len(s)-len(p)-1, -1, -1):
            self.change_count(s_arr, s[i+len(p)], -1)
            self.change_count(s_arr, s[i], 1)
            if p_arr == s_arr:
                res.append(i)
             
        return res
    
    
    def change_count(self, arr: List[int], char: str, count: int) -> None:
        index = ord(char) - 97
        arr[index] += count
        
    
    
    
    
    
    
    
