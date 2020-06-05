class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = heights.copy()
        target.sort()
        counter = 0
        for i in range(len(heights)):
            if heights[i] != target[i]:
                counter += 1
        return counter
