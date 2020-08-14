class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.recurse(1, n, k, [], res)
        return res
  
    
    def recurse(self, index: int, n: int, k: int, cur: List[int], res: List[List[int]]) -> None:
        if len(cur) == k:
            res.append(cur)
            return
        if index > n:
            return
        with_index = cur + [index]
        self.recurse(index+1, n, k, with_index, res)
        self.recurse(index+1, n, k, cur, res)
        return
       
