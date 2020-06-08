class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        Cpositions = []
        for i in range(len(S)):
            if S[i] == C:
                Cpositions.append(i)
        res = []
        for i in range(len(S)):
            print(S[i])
            if S[i] == C:
                res.append(0)
                continue
            minDistance = abs(i - Cpositions[0])
            for j in range(1, len(Cpositions)):
                minDistance = min(abs(i - Cpositions[j]), minDistance)
            res.append(minDistance)
        return res
