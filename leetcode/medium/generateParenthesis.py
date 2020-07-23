class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string = [None]*(n*2)
        res = []
        self.addParen(res, n, n, string, 0)
        return res
        
    
    def addParen(self, res: List[int], leftRem: int, rightRem: int, string: List[str], index: int) -> None:
        if leftRem < 0 or rightRem < leftRem:
            return
        if leftRem == 0 and rightRem == 0:
            res.append("".join(string))
        else:
            string[index] = "("
            self.addParen(res, leftRem-1, rightRem, string, index+1)
            string[index] = ")"
            self.addParen(res, leftRem, rightRem-1, string, index+1)
        
