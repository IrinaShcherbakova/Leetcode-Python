class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        small = 1
        large = n - 1
        while self.containsZero(large) or self.containsZero(small):
            small += 1
            large -= 1
        return [small, large]
    
    
    
    def containsZero(self, num: int) -> bool:
        string = str(num)
        for char in string:
            if char == '0':
                return True
        return False
