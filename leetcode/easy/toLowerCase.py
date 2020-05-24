class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for char in str:
            if char.isupper():
                res = res + chr(ord(char) + 32)
            else:
                res = res + char
        return res
