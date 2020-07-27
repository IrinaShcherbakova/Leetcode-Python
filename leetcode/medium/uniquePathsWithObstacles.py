class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = []
        for i in range(len(obstacleGrid)):
            memo.append([0]*len(obstacleGrid[0]))
        return self.findPaths(obstacleGrid,0,0,memo)
    
    
    def findPaths(self, obstacleGrid: List[List[int]], r: int, c: int, memo: List[int]) -> int:
        if r >= len(obstacleGrid) or c >= len(obstacleGrid[0]):
            return 0
        if obstacleGrid[r][c] == 1:
            return 0
        if memo[r][c] > 0:
            return memo[r][c]
        if r == len(obstacleGrid)-1 and c == len(obstacleGrid[0])- 1: # hit finish
            return 1
        memo[r][c] = self.findPaths(obstacleGrid,r+1,c,memo) + self.findPaths(obstacleGrid,r,c+1,memo)
        return memo[r][c]
        
        
