class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = [0] * 26
        for char in s:
            letters[ord(char)-97] += 1
        # print(letters)
        for char in t:
            letters[ord(char)-97] -= 1
        # print(letters)
        for i, count in enumerate(letters):
            if count < 0:
                return chr(i+97)
