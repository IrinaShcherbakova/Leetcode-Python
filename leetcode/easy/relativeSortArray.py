class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for num in arr2:
            for i in range(len(arr1)):
                if num == arr1[i]:
                    ans.append(num)
                    arr1[i] = None
        rest = []
        for num in arr1:
            if num:
                rest.append(num)
        rest.sort()
        ans = ans + rest
        return ans
