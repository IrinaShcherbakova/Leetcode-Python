class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        seen_odd = False
        longest = 0
        for key in counts:
            if counts[key] % 2 == 0:
                longest += counts[key]
            elif not seen_odd:
                longest += counts[key]
                seen_odd = True
            else:
                longest += (counts[key]-1)
        return longest
