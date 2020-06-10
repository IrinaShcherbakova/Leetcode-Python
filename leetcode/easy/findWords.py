class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            prevRow = self.rowNumber(word[0])
            isOneRow = True
            for i in range(1, len(word)):
                if self.rowNumber(word[i]) != prevRow:
                    isOneRow = False
                    break
            if isOneRow:
                ans.append(word)
        return ans
                
                              
    def rowNumber(self, char: str) -> int:
        one = {'q', 'w', 'e', 'r', 't', 'u', 'i', 'o', 'p', 'y'}
        two = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        if char.lower() in one:
            return 1
        elif char.lower() in two:
            return 2
        return 3
        
                
