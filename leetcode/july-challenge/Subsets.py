class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.allSubsets(0, nums, [], res)
        return res
        
    
    def allSubsets(self, pos: int, nums: List[int], cur: List[int], res: List[List[int]]) -> None:
        if pos == len(nums):
            res.append(cur)
            return
        temp = cur.copy()
        temp.append(nums[pos])
        self.allSubsets(pos+1, nums, temp, res)
        self.allSubsets(pos+1, nums, cur, res)
        return
