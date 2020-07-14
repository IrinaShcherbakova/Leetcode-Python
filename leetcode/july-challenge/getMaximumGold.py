class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        withGold = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and j == 0 or j == len(grid[0])-1:
                    withGold.append([i,j])
                    continue
                if grid[i][j] > 0 and i == 0 or i == len(grid) - 1:
                    withGold.append([i,j])
                    continue
                if grid[i][j] > 0 and self.adjacentNoGold(grid, i, j) == 3:
                    withGold.append([i,j])
                    continue      
        self.sortFun(grid, withGold)
        print(withGold)
        maxGold = 0
        # print(grid)
        for start in withGold:
            # gridCopy = deepcopy(grid)
            # print(gridCopy)
            gold = self.dfs(grid, start[0], start[1])
            print("row %s, col %s, gold %s" %(start[0],start[1],gold))
            maxGold = max(maxGold, gold)
        return maxGold
    
    def sortFun(self, grid: List[List[int]], target: List[List[int]] ) -> None:
        for i in range(len(target)-1):
            maxInd = i
            for j in range(i+1, len(target)):
                r, c = target[j][0], target[j][1]
                maxr, maxc = target[maxInd][0], target[maxInd][1]
                if grid[r][c] > grid[maxr][maxc]:
                    maxInd = j
            if maxInd != i:
                target[i], target[maxInd] = target[maxInd], target[i]
        return
    
    def adjacentNoGold(self, grid: List[List[int]], r: int, c: int) -> int:
        top = (1 if r < 0 or grid[r-1][c] == 0 else 0)
        bottom = (1 if r >= len(grid) or grid[r+1][c] == 0 else 0)
        right = (1 if c >= len(grid[0]) or grid[r][c+1] == 0 else 0)
        left = (1 if c < 0 or grid[r][c-1] == 0 else 0)
        return top + bottom + right + left
        
    def dfs(self, gridCopy: List[List[int]], r: int, c: int) -> int:
        # print(grid)
        if r >= len(gridCopy) or r < 0:
            return 0
        if c >= len(gridCopy[0]) or c < 0:
            return 0
        if gridCopy[r][c] == 0:
            return 0
        cur = gridCopy[r][c]
        # print(res)
        gridCopy[r][c] = 0
        gold = max(self.dfs(gridCopy, r, c-1), self.dfs(gridCopy, r, c+1), self.dfs(gridCopy, r-1, c), self.dfs(gridCopy, r+1, c))
        gridCopy[r][c] = cur
        return cur + gold
    
    
    
