class Solution:
    def frequencySort(self, s: str) -> str:
        counts ={}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        res = ""
        for char in sorted(counts, key = counts.get, reverse = True):
            res += (counts[char]*char)
        return res
                
