class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first = (True if word[0].isupper() else False)
        capitalCounter = 0
        for i in range(0, len(word)):
            if word[i].isupper():
                capitalCounter += 1
                if capitalCounter - 1 != i:
                    return False
        if capitalCounter <= 1:
            return (True if capitalCounter == 0 else first)
        return capitalCounter == len(word)
            
