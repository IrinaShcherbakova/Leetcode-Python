class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit = int(len(arr) * 0.25)
        count = i = 1
        while i < len(arr):
            count = 1
            while i < len(arr) and arr[i] == arr[i-1]:
                count += 1
                if count > limit:
                    return arr[i]
                i += 1
            if count > limit:
                return arr[i-1]
            i += 1
        return arr[-1]
