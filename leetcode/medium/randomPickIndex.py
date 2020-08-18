class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)
        

    def pick(self, target: int) -> int:
        index = random.randint(0, self.length-1)
        while self.nums[index] != target:
            index = random.randint(0, self.length-1)
        return index
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
