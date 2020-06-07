class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = [0]*26
        for char in chars:
            counts[ord(char)-97] += 1
        res = 0
        for word in words:
            sorted_chars = sorted(word)
            isValid = True
            i = 0
            while i < len(sorted_chars):
                charCounter = 1
                while i+1 < len(sorted_chars) and sorted_chars[i] == sorted_chars[i+1]:
                    charCounter += 1
                    i += 1
                if counts[ord(sorted_chars[i])-97] < charCounter:
                    isValid = False
                    break
                i += 1
            if isValid:
                res += len(sorted_chars)
        return res
                
            
