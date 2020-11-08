class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        # explore all lands which are not enclaves
        for c in range(len(A[0])):
            self.not_enclave(A, 0, c)
            self.not_enclave(A, len(A)-1, c)
        for r in range(len(A)):
            self.not_enclave(A, r, 0)
            self.not_enclave(A, r, len(A[0])-1)

        # count enclaves
        enclaves = 0
        for i in range(1, len(A)-1):
            for j in range(1, len(A[0])-1):
                if A[i][j] == 1:
                    enclaves += 1
        return enclaves
    
      
    def not_enclave(self, A: List[List[int]], r: int, c: int) -> None:
        if r < 0 or r >= len(A) or c < 0 or c >= len(A[0]):
            return
        if A[r][c] == 0 or A[r][c] == -1:
            return
        A[r][c] = -1
        self.not_enclave(A, r+1, c)
        self.not_enclave(A, r-1, c)
        self.not_enclave(A, r, c+1)
        self.not_enclave(A, r, c-1)
        return 
          

