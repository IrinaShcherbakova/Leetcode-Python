class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        newWord = 1
        i = 0
        while i < len(sentence):
            if sentence[i] == ' ':
                newWord += 1
                i += 1
            isPrefix = True
            for j in range(len(searchWord)):
                if i == len(sentence):
                    return -1
                elif sentence[i] == ' ':
                    isPrefix = False
                    break
                elif searchWord[j] != sentence[i]:
                    isPrefix = False
                    break
                i += 1
            if isPrefix:
                return newWord
            while i < len(sentence) and sentence[i] != ' ':
                i += 1
        return -1
