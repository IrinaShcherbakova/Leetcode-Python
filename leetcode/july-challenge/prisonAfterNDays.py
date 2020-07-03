class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = N % 14
        if N == 0:
            N = 14
        for i in range(N):
            temp = [0]
            for j in range(1, len(cells) - 1):
                if cells[j-1] == cells[j+1]:
                    temp.append(1)
                else:
                    temp.append(0)
            temp.append(0)
            cells = temp
        return cells
