class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.form_sum(candidates, 0, target, [], res)
        return res
    
    
    def form_sum(self, candidates: List[int], index: int, target: int, nums: List[int], res: List[List[int]]) -> None:
        if index == len(candidates):
            return
        
        sum_so_far = sum(nums)
        if sum_so_far > target:
            return
        
        cur = candidates[index]
        
        if cur > target:
            return self.form_sum(candidates, index+1, target, nums, res)
        
        if sum_so_far + cur == target:
            res.append(nums + [cur])
            
        with_cur = nums + [cur]
        self.form_sum(candidates, index, target, with_cur, res)
        self.form_sum(candidates, index+1, target, nums, res)
        return
           
