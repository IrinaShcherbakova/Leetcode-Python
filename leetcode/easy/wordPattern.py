class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        patterns = {}
        str = str.split()
        if len(str) != len(pattern):
            return False
        i = 0
        for letter in pattern:
            if letter not in patterns:
                if str[i] in patterns.values():
                    return False
                patterns[letter] = str[i]
            else:
                if patterns[letter] != str[i]:
                    return False
            i += 1
        return True
