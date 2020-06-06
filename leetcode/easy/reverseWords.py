class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(" ")
        ans = ""
        for index, word in enumerate(sList):
            if index != 0:
                ans = ans + " "
            i = len(word) - 1
            while i >= 0:
                ans = ans + word[i]
                i -= 1
        return ans
