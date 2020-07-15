class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        #read all words without trailing whitespaces
        while i < len(s):
            i, word = self.readWord(s, i)
            if len(word) > 0:
                words.append(word)
        #reverse words in a string
        i, j = 0, len(words)-1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        #return result as a string
        ans = ""
        for i, word in enumerate(words):
            if i != len(words) - 1:
                ans = ans + word + " "
            else:
                ans += word
        return ans
                     
    
    def readWord(self, s: str, i: int) -> tuple:
        ans = ""
        #skip all leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1
        #copy string word by word to answer string
        while i < len(s) and s[i] != ' ':
            ans += s[i]
            i += 1
        #return index at which we stop and answer string
        return i, ans
