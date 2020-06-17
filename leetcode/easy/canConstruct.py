class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterCount = [0] * 26
        
        for char in ransomNote:
            letterCount[ord(char)-97] += 1
        
        for char in magazine:
            letterCount[ord(char)-97] -= 1
        
        #if letterCount contains positive count => we cannot construct ransomNote
        for count in letterCount:
            if count > 0:
                return False
        return True
