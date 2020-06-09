class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        for num in arr:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
        lucky = []
        for count in counts:
            if count == counts[count]:
                lucky.append(count)
        if len(lucky) == 0:
            return -1
        return max(lucky)
