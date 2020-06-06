class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counter = {}
        for i in range(len(mat)):         
            counter[i] = self.numberOfOnes(mat[i])
        ans = sorted(counter, key=counter.get)
        return ans[0:k]
        
    
    def numberOfOnes(self, row: List[int]) -> int:
        res = 0
        for num in row:
            if num == 1:
                res += 1
            else:
                return res
        return res
