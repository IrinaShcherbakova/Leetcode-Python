class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[start]:
                cur_power = i - start 
                max_power = max(max_power, cur_power)
                start = i
        max_power = max(max_power, len(s) - start)
        return max_power
