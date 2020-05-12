class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = candies[0]
        for i in range(1, len(candies)):
            if candies[i] > maxCandies:
                maxCandies = candies[i]
        result = []
        for kid in candies:
            if kid + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
