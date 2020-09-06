class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        substr = ""
        for i in range(len(s)//2):
            substr += s[i]
            if self.construct_from_substr(substr, s[i+1:len(s)]):
                return True
        return False
    
    
    def construct_from_substr(self, substr: str, string: str):
        if len(string) < len(substr):
            return False
        if len(string) % len(substr) > 0:
            return False
        if len(string) == len(substr):
            return string == substr
        if string.startswith(substr):
            tail = string[len(substr):len(string)]
            return self.construct_from_substr(substr, tail)
        return False
        
            
            
            
            
            
            
            
            
            
        
