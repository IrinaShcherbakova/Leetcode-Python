class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxEl = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > maxEl:
                temp = arr[i]
                arr[i] = maxEl
                maxEl = temp
            else:
                arr[i] = maxEl
        return arr
