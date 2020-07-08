class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        arr = self.charFreq(pattern)
        res = []
        for word in words:
            temp = self.charFreq(word)
            if self.isEqual(arr, temp):
                res.append(word)
        return res
            
          
    def charFreq(self, word: str) -> List[int]:
        arr = []
        start = 0
        seen = {}
        for char in word:
            if char not in seen:     
                seen[char] = start
                start += 1
            arr.append(seen[char])
        return arr
    
    
    def isEqual(self, one: List[int], two: List[int]) -> bool:
        for i in range(len(one)):
            if one[i] != two[i]:
                return False
        return True
