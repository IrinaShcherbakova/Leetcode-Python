class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        values = set()
        for val in arr:
            if val * 2 in values:
                return True
            if val % 2 == 0 and val / 2 in values:
                return True
            values.add(val)
        return False
        
