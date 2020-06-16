class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        while True:
            while numbers[right] + numbers[left] > target:
                right -= 1
            res = self.findSum(numbers, target, left, right) 
            if len(res) > 0:
                return res
            left += 1
 
            
    def findSum(self, numbers: List[int], target: int, left: int, right: int) -> List[int]:
        for i in range(left, right + 1):
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
        return []
            
