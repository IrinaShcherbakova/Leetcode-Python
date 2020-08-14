class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            next_row = []
            for i, num in enumerate(triangle[row]):
                num = min(prev_row[i], prev_row[i+1]) + num
                next_row.append(num)
            prev_row = next_row
        return prev_row[0]
