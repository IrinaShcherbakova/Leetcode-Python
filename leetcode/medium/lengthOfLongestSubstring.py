class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = current = start = 0
        for i, char in enumerate(s):
            # print("longest %s" %longest)
            # print("current %s" %current)
            # print("start %s" %start)

            if (char in seen and seen[char] < start) or char not in seen:
                seen[char] = i
                current += 1
            else:
                # print("new substring from %s" %char)
                longest = max(longest, current)
                start = seen[char] + 1
                current = i - seen[char]
                seen[char] = i
        return max(longest, current)
