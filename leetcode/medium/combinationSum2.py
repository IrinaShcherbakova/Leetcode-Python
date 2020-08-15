class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        self.recurse(candidates, 0, target, [], res)
        return res
    
        
    def recurse(self, candidates: List[int], index: int, target: int, cur: List[int], res: List[List[int]]) -> None:
        cur_sum = sum(cur)
        if cur_sum == target:
            res.append(cur)
            return
        if index >= len(candidates):
            return
        if cur_sum > target:
            return
        
        if cur_sum + candidates[index] <= target:
            with_current_index = cur + [candidates[index]]
            self.recurse(candidates, index+1, target, with_current_index, res)
        
        index += 1
        while index < len(candidates) and candidates[index] == candidates[index-1]:
            index += 1
         
        self.recurse(candidates, index, target, cur, res)    
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
