class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        copyArr = arr.copy()
        copyArr.sort()
        ranks = {}
        curRank = 1
        for num in copyArr:
            if num not in ranks:
                ranks[num] = curRank
                curRank += 1
        res = []
        #print(ranks)
        for num in arr:
            res.append(ranks[num])
        return res
