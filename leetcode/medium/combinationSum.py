class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.recurse(candidates, 0, [], target, res)
        return res
        
    
    def recurse(self, candidates: List[int], index: int, seq: List[int], target: int, res: List[List[int]]) -> None:
        if index == len(candidates):
            return
        cur_sum = sum(seq)
        if cur_sum > target:
            return
        
        if cur_sum + candidates[index] == target:
            res.append(seq+[candidates[index]])
            self.recurse(candidates, index+1, seq, target, res)
        elif cur_sum + candidates[index] < target:
            # we have 2 options: recurse with the current index, recurse with next index
            self.recurse(candidates, index, seq + [candidates[index]], target, res)
            self.recurse(candidates, index+1, seq, target, res)
        else:
            # recurse without the current index
            self.recurse(candidates, index+1, seq, target, res)
        return
        
    
    
    
        
