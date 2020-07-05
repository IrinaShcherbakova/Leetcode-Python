class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        one = self.toBinary(x)
        two = self.toBinary(y)
        if len(one) > len(two):
            two = self.padZeros(two, len(one) - len(two))
        else:
            one = self.padZeros(one, len(two) - len(one))
        count = 0
        for i in range(len(one)):
            if one[i] != two[i]:
                count += 1
        return count
    
    
    def toBinary(self, num: int) -> List[int]:
        res = []
        while num > 0:
            rem = num % 2
            res.append(rem)
            num = num // 2
        return res
    
    
    def padZeros(self, l: List[int], zeros: int) -> List[int]:
        for i in range(zeros):
            l.append(0)
        return l
