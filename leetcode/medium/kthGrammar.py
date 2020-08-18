class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        prev_k = []
        K -= 1
        for i in range(N):
            prev_k.append(True if K % 2 == 0 else False)
            if K % 2 == 0:
                K = K // 2
            else:
                K = (K-1) // 2
        prev_k.pop()
        return self.recurse(prev_k, 0)
    
    
    def recurse(self, prev_k: List[int], val: int) -> int:
        if not prev_k:
            return val
        prev = prev_k.pop()
        left = (0 if val == 0 else 1) 
        right = (1 if val == 0 else 0)
        if prev:
            return self.recurse(prev_k, left)
        return self.recurse(prev_k, right)
    
    
    
    
    
    
                
                
