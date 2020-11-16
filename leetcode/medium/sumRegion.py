class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = []
        for row in matrix:
            r = []
            running_sum = 0
            for num in row:
                running_sum += num
                r.append(running_sum)
            self.m.append(r)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = 0
        for i in range(row1, row2+1):
            region_sum += self.m[i][col2]
            if col1 - 1 >= 0:
                region_sum -= self.m[i][col1-1]
        return region_sum
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
