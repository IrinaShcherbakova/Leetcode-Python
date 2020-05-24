class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = []
        for pair in paths:
            source.append(pair[0])
        for pair in paths:
            if pair[1] not in source:
                return pair[1]
