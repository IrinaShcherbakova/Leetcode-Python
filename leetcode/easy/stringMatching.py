class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # print(words[i])
                # print(words[j])
                res = self.isSubString(words[j], words[i])
                if res == 1 and words[j] not in ans:
                    ans.append(words[j])
                if res == 2 and words[i] not in ans:
                    ans.append(words[i])
        return ans
    
    
    def isSubString(self, one: str, two: str) -> int:
       # print("one is %s two is %s " %(one, two))
        smaller = (one if len(one) < len(two) else two)
        longer = (one if len(one) >= len(two) else two)
        #print("smaller is %s longer is %s " %(smaller, longer))
        if smaller not in longer:
            return 0
        return (1 if smaller == one else 2)
       
    
    
    
    
    
    
