class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for num in A:
            if num % 2 == 0:
                evenSum += num
        res = []
        for query in queries:
            val = query[0]
            index = query[1]
            newVal = A[index] + val
            if A[index] %2 == 0 and newVal % 2 == 0:
                evenSum = evenSum - A[index] + newVal
            elif A[index] %2 != 0 and newVal % 2 == 0:
                evenSum = evenSum + newVal
            elif A[index] %2 == 0 and newVal % 2 != 0:
                evenSum -= A[index]
            A[index] = newVal
            res.append(evenSum)
        return res
