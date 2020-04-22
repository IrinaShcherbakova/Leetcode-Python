class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        result = []
        start = 0
        count = 1
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
                continue
            if count >= 3:
                result.append([start, i-1])
            count = 1
            start = i
        if count >= 3:
                result.append([start, len(S) - 1])
        return result
