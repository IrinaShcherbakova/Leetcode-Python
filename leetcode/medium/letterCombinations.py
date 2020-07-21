class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",'7': "pqrs", '8': "tuv", '9': "wxyz"}
        
        res = []
        i = 0
        
        #skip all 1's in the beginning
        while i < len(digits) and digits[i] == '1':
            i += 1
        if i == len(digits):
            return res
        
        firstButton = mapping[digits[i]]
        for letter in firstButton:
            self.combine(letter, digits, i+1, res, mapping)
        return res
                
    
    def combine(self, stringSoFar: str, digits: str, i: int, res: List[str], mapping: dict) -> None:
        
        if i >= len(digits):
            res.append(stringSoFar)
            return None
            
        #skip 1
        if digits[i] == '1':
            return self.combine(stringSoFar, digits, i+1, res)
        
        button = mapping[digits[i]]
    
        for letter in button:
            extendedString = stringSoFar + letter
            self.combine(extendedString, digits, i+1, res, mapping)
    
        return None
 
            
        
