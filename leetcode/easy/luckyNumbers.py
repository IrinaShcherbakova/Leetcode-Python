class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for row in matrix:
            rowMin = row[0]
            pos = 0
            for i in range(1, len(row)):
                if row[i] < rowMin:
                    rowMin = row[i]
                    pos = i
            #print(rowMin)
            isLucky = True
            for col in matrix:
                if col[pos] > rowMin:
                    isLucky = False
                    break
            if isLucky: ans.append(rowMin)
        return ans
            
