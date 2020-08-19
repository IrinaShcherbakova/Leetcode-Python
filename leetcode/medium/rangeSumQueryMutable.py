class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = self.fill_sums(nums)
        self.updates = {}  #stores index and difference with the original value

        
    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.updates[i] = diff
        
        
    def sumRange(self, i: int, j: int) -> int:
        range_sum = self.nums[i] + self.sums[j] - self.sums[i]
        for index in self.updates:
            if index >= i and index <= j:
                range_sum += self.updates[index]
        return range_sum
        
               
    def fill_sums(self, nums: List[int]) -> List[int]:
        sums = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            sums.append(cur_sum)
        return sums
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
