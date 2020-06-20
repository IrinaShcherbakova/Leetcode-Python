class NumArray:

    def __init__(self, nums: List[int]):
        self.sumAtIndex = []
        cur = 0
        for num in nums:
            cur += num
            self.sumAtIndex.append(cur)
        
        
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sumAtIndex[j]
        return self.sumAtIndex[j] - self.sumAtIndex[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
