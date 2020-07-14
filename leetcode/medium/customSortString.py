class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order = {}
        i = 0
        for char in S:
            order[char] = i
            i += 1
        #selection sort for T
        t = list(T)
        for i in range(len(t)-1):
            # print("t[i] is %s" %t[i])
            if t[i] not in order:
                continue
            minInd = i
            for j in range(i+1, len(t)):
                # print(t[j])
                if t[j] in order and order[t[j]] < order[t[minInd]]:
                    minInd = j
            if minInd != i:
                t[minInd], t[i] = t[i], t[minInd]
        return "".join(t)
                    
                
