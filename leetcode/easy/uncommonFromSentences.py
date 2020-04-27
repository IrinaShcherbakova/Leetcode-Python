class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        result = []
        listA = A.split()
        listB = B.split()
        for word in listA:
            if listA.count(word) == 1 and word not in listB:
                result.append(word)
        for word in listB:
            if listB.count(word) == 1 and word not in listA:
                result.append(word)
        return result
