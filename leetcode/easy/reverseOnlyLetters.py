class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        string = list(S)
        i = 0
        j = len(string) - 1
        while i < j:
            if not string[i].isalpha():
                i += 1
                continue
            if not string[j].isalpha():
                j -= 1
                continue
            temp = string[i]
            string[i] = string[j]
            string[j] = temp
            i += 1
            j -= 1
        return ''.join(string)
