class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I'}
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and s[i] not in vowels:
                i += 1
            while j >= 0 and s[j] not in vowels:
                j -= 1
            if i >= j:
                return "".join(s)
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        return "".join(s)
