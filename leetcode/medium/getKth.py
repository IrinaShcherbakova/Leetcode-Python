class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {}
        res = []
        for i in range(lo, hi+1):
            powers[i] = self.getPower(i)
            res.append(i)
        #sort res array with selection sort
        for i in range(len(res)-1):
            # print("res[i] is %s, power is %s" %(res[i], powers[res[i]]))
            jMin = i
            for j in range(i+1, len(res)):
                if powers[res[j]] < powers[res[jMin]]:
                    jMin = j
                    continue
                if powers[res[j]] == powers[res[jMin]] and res[j] < res[jMin]:
                    jMin = j
            if jMin != i:
                # print("swap with %s" %res[jMin])
                res[i], res[jMin] = res[jMin], res[i]
                # print("new res %s" % res)
        # print(res)
        return res[k-1]
                     
    
    def getPower(self, num: int) -> int:
        power = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 +1
            power += 1
        return power
