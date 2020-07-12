class Solution:
    def reverseBits(self, n: int) -> int:
        total, count = 0, 0
        res = []
        while n != 0:
            n, rem = divmod(n, 2)
            #res.append(rem)
            total = (total*2) + rem
            count += 1
        # print(res)
        # print(len(res))
        for i in range(count, 32):
            total *= 2
        return total
        
