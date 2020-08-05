class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.transform(S, 0, res)
        return res
    
    
    def transform(self, S: str, index: int, res: List[int]) -> None:
        if index == len(S):
            res.append(S)
            return
        
        char = S[index]
        
        if char.islower():
            up = char.upper()
            upper_case_str = S[0:index] + up + S[index+1:]
            self.transform(upper_case_str, index+1, res)
        
        elif char.isupper():
            low = char.lower()
            low_case_str = S[0:index] + low + S[index+1:]
            self.transform(low_case_str, index+1, res)
        
        return self.transform(S, index+1, res)
        
