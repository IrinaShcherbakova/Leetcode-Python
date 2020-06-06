class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            for j in range(len(arr) - i - 1):
                one = self.numberOfOnes(arr[j])
                two = self.numberOfOnes(arr[j+1])
                if one > two:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                elif one == two and arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    
    def numberOfOnes(self, num: int) -> int:
        res = 0
        while num > 0:
            res = res + (num % 2)
            num = num // 2
        return res
