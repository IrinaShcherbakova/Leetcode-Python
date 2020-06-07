class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        counter = 0
        maxAccepted = None
        for i in range(len(arr1)):
            if maxAccepted and arr1[i] > maxAccepted:
                maxAccepted = arr1[i]
                counter += 1
                continue
            isValid = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    isValid = False
            if isValid:
                counter += 1
        return counter
