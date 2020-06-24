class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        oddFound = False
        longest = 0
        for char in letters:
            if letters[char] % 2 == 0:
                longest += letters[char]
                continue
            if not oddFound:
                longest += letters[char]
                oddFound = True
            else:
                longest = longest + letters[char] - 1
        return longest
