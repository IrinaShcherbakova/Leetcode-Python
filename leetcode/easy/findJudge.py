class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustCounts = {}
        seenA = set()
        for pair in trust:
            a = pair[0]
            b = pair[1]
            if a in trustCounts:
                trustCounts.pop(a)
            seenA.add(a)
            if b in seenA:
                continue
            if b in trustCounts:
                trustCounts[b] += 1
            else:
                trustCounts[b] = 1
        maxTrust, judge = 0, N
        for person in trustCounts:
            if trustCounts[person] > maxTrust:
                maxTrust = trustCounts[person]
                judge = person
        return (judge if maxTrust == N - 1 else -1)
