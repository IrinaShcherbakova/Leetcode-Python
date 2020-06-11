class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(nums)
        cols = len(nums[0])
        if rows * cols != r * c:
            return nums
        res = []
        newRow = []
        index = 0
        for row in nums:
            for col in row:
                if index == c:
                    res.append(newRow)
                    newRow = []
                    index = 0
                newRow.append(col)
                index += 1
        res.append(newRow)
        return res
                    
