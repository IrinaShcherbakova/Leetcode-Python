class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        elements = {}
        n = len(A) // 2
        for num in A:
            if num in elements:
                count = elements[num]
                if count + 1 == n:
                    return num
                elements[num] = count + 1
            else:
                elements[num] = 1
