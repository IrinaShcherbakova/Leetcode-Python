class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        previous_row = [1, 1]
        for i in range(2, rowIndex+1):
            next_row = [1] * (i+1)
            left, right = 1, len(next_row) - 2
            j = 0
            while left <= right:
                num = previous_row[j] + previous_row[j+1]
                next_row[left] = num
                next_row[right] = num
                j += 1
                left += 1
                right -= 1
            previous_row = next_row
        return previous_row
            
