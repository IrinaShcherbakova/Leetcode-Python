class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if self.isSelfDividing(i):
                res.append(i)
        return res
    
    def isSelfDividing(self, i: int) -> bool:
        string = str(i)
        for number in string:
            if int(number) == 0:
                return False
            if i % int(number) != 0:
                return False
        return True
            
