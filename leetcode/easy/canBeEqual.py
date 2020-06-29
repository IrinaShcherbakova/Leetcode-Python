class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counts = {}
        for num in target:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num in arr:
            if num not in counts:
                return False
            if counts[num] == 1:
                counts.pop(num)
            else:
                counts[num] -= 1
        return len(counts) == 0
