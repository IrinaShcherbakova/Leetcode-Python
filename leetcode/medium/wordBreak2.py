class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        substrings = {}
        return self.break_word(s, wordDict, substrings)
            
     
    def break_word(self, s: str, wordDict: List[str], substrings: dict) -> bool:
        if not s:
            return True
        if s in substrings:
            return substrings[s]     
        # print("consider %s" %s)
        for word in wordDict:
            if s.startswith(word):
                segment = s[len(word):len(s)]
                # print(segment)
                can_be_broken = self.break_word(segment, wordDict, substrings)
                if can_be_broken:
                    substrings[s] = True
                    return True
        substrings[s] = False
        return False
