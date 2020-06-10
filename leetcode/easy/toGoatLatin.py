class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = ""
        i = 0
        counter = 1
        #invariant: i starts with new word
        while i < len(S):
            firstLetter = None
            if S[i].lower() in vowels:
                ans = ans + S[i]
                i += 1
            else:
                firstLetter = S[i]
                i += 1
            while i < len(S) and S[i] != ' ':
                ans = ans + S[i]
                i += 1
            if firstLetter:
                ans = ans + firstLetter
            ans = ans + "ma" + ('a'*counter)
            if i < len(S):
                ans = ans + S[i]
                i += 1
                counter += 1
        return ans
            
            
