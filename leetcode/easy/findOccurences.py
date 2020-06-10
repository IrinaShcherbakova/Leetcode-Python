class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        i = 0
        #invariant: i always starts with a new word
        while i < len(text):
            if i < 0:
                break
        
            if text[i] != first[0]:
                i = self.nextWord(text, i)
                continue
            
            #check first word
            if self.isEqualWords(text, i, first):
                i = i + len(first) + 1
            else:
                i = self.nextWord(text, i)
                continue
            
            #check second word
            if self.isEqualWords(text, i, second):
                i = i + len(second) + 1
                third = ""
                k = i
                while k < len(text) and text[k] != ' ':
                    third = third + text[k]
                    k += 1
                if len(third) > 0:
                    ans.append(third)          
        return ans
                
            
    def nextWord(self, text: str, i: int) -> int:
        if i >= len(text):
            return -1
        while i < len(text) and text[i] != ' ':
            i += 1
        if i == len(text):
            return -1
        if text[i] == ' ':
            return i+1
        
        
    def isEqualWords(self, text: str, i: int, word: str) -> bool:
        if len(text) - i < len(word):
            return False
        j = 0
        while j < len(word):
            if text[i] != word[j]:
                return False
            i += 1
            j += 1
        return True
            
        
        
        
        
