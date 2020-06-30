class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = {}
        maxCount, i = 0, 0
        mostFreq = None
        while i < len(paragraph):
            while i < len(paragraph) and not paragraph[i].isalpha():
                i += 1
            word = self.parse(paragraph, i)
            if word not in banned:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
                if counts[word] > maxCount:
                    maxCount = counts[word]
                    mostFreq = word
            i += len(word)
        return mostFreq
        
  
    def parse(self, par: str, start: int) -> str:
        ans = []
        for i in range(start, len(par)):
            if 'A' <= par[i] <= 'Z':
                ch = chr(ord(par[i]) + 32)
                ans.append(ch)
            elif 'a' <= par[i] <= 'z':
                ans.append(par[i])
            else:
                break
        return "".join(ans)
        
