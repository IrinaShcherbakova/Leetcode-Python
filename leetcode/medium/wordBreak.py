class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return (True if len(self.constructSentence(s, wordDict, memo)) > 0 else False)    
    
    def constructSentence(self, s: str, wordDict: List[str], memo: dict) -> List[str]:
        if s in memo:
            return memo[s]
        
        res = []
        if len(s) == 0:
            res.append("")
            return res
                  
        for word in wordDict:
            if s.startswith(word):
                suffixes = self.constructSentence(s[len(word):], wordDict, memo)
                for suffix in suffixes:
                    sentence = ""
                    if len(suffix) > 0:
                        sentence = word + ' ' + suffix
                    else:
                        sentence = word + suffix
                    res.append(sentence)
        memo[s] = res
        return res
            
        
