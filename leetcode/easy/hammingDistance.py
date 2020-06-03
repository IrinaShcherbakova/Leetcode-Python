class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        one = self.toBinary(x)
        two = self.toBinary(y)
        count = 0
        longer = (len(one) if len(one) > len(two) else len(two))
        for i in range(longer-1, -1, -1):
            print(i)
            if i >= len(one):
                if two[i] != 0:
                    count += 1
                continue
            if i >= len(two):
                if one[i] != 0:
                    count += 1
                continue
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
