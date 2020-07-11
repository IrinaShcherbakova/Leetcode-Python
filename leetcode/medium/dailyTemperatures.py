class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            # print("cur temp is %s, maxTemp is %s" % (T[i], T[maxTemp]))
            if T[i] == T[i+1]:
                res[i] = (0 if res[i+1] == 0 else res[i+1]+1)
            elif T[i] < T[i+1]:
                res[i] = 1
            else:
                res[i] = self.findGreaterTemp(T, res, i)
        return res
            
    
    def findGreaterTemp(self, T: List[int], res: List[int], start: int) -> int:
        i = start + 1
        while i < len(T) and T[i] < T[start]:
            if res[i] == 0:
                return 0
            i += res[i]
        if i < len(T) and T[i] == T[start]:
            return (0 if res[i] == 0 else res[i]+i-start)
        return (0 if i >= len(T) else i - start)
        
