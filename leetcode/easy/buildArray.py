class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        curIndex = 0
        for i in range(1, n+1):
            if target[curIndex] == i:
                res.append("Push")
                curIndex += 1
            else:
                res.append("Push")
                res.append("Pop")
            if curIndex == len(target):
                break
        return res
