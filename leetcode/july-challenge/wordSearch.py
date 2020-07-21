class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, word, 0, i, j):
                    return True
        return False
    
    
    
    def dfs(self, board: List[List[str]], word: str, i: index, r: int, c: int) -> bool:
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return False
        # print("visit %s-%s, search for %s" %(r,c,word[i]))
        # print("value of cell is %s" %board[r][c])
        if i > 0 and board[r][c] != word[i]:
            return False
        if board[r][c] == '0':
            return False
        prevValue = board[r][c]
        found = False
        if prevValue == word[i]:
            board[r][c] = '0'
            found = self.dfs(board, word, i+1, r+1, c) or self.dfs(board, word, i+1, r-1, c) or self.dfs(board, word, i+1, r, c+1) or self.dfs(board, word, i+1, r, c-1)
        else:
            found = self.dfs(board, word, i, r+1, c) or self.dfs(board, word, i, r-1, c) or self.dfs(board, word, i, r, c+1) or self.dfs(board, word, i, r, c-1)
        board[r][c] = prevValue
        return found
        
        
