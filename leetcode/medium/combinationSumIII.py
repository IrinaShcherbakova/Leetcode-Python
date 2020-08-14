class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.recurse(1, k, n, [], res)
        return res
    
    
    def recurse(self, index: int, k: int, n: int, cur: List[int], res: List[List[int]]) -> None:
        if len(cur) == k and sum(cur) == n:
            res.append(cur)
            return
        if index > 9:
            return
        if len(cur) >= k:
            return
        
        # recurse using the current index
        with_index = cur + [index]
        self.recurse(index+1, k, n, with_index, res)
        
        # recurse without using the current index
        self.recurse(index+1, k, n, cur, res)
        
        return
