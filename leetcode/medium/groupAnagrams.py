class Anagram:
    
    def __init__(self, word: str, letterCount: dict):
        self.pattern = letterCount
        self.length = len(word)
        self.words = [word]
    
    def isEqual(self, letterCount: dict) -> bool:
        for ch in letterCount:
            if ch not in self.pattern or self.pattern[ch] != letterCount[ch]:
                return False
        return True
    
    def add(self, word: str, letterCount: List[int]) -> bool:
        if self.length != len(word):
            return False
        if self.isEqual(letterCount):
            self.words.append(word)
            return True
        return False
        
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        #group anagrams by size
        anagrams = {}        
        first = Anagram(strs[0], self.letterPattern(strs[0]))
        anagrams[len(strs[0])] = [first]
        for i in range(1, len(strs)):
            word = strs[i]
            length = len(word)
            letters = self.letterPattern(word)
            if length not in anagrams:
                anagrams[length] = [Anagram(word, letters)]
            else:
                for anagram in anagrams[length]:
                    if anagram.add(word, letters):
                        break
                else:
                    anagrams[length].append(Anagram(word, letters))
        res = []
        for length in anagrams:
            patterns = anagrams[length]
            for pattern in patterns:
                res.append(pattern.words)
        return res
    
    def letterPattern(self, word: str) -> dict:
        pattern = {}
        for ch in word:
            if ch in pattern:
                pattern[ch] += 1
            else:
                pattern[ch] = 1
        return pattern
            
            
        
        
        
        
        
        
        
        
        
        
        
