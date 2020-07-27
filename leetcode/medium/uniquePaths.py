class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = []
        for i in range(m):
            memo.append([0]*n)
        return self.findPaths(m,n,0,0,memo)
    
    
    def findPaths(self, m: int, n: int, r: int, c: int, memo: List[int]) -> int:
        if r >= m or c >= n:
            return 0
        if r == m - 1 or c == n - 1:
            return 1
        if memo[r][c] > 0:
            return memo[r][c]
        memo[r][c] = self.findPaths(m,n,r+1,c,memo) + self.findPaths(m,n,r,c+1,memo)
        return memo[r][c]
        
        
