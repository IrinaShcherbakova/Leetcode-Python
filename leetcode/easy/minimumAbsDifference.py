class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDistance = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i+1]-arr[i] < minDistance:
                minDistance = arr[i+1] - arr[i]
        ans = []
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == minDistance:
                ans.append([arr[i],arr[i+1]])
        return ans
