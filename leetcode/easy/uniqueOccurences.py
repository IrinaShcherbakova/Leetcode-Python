class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1
        counters = []
        for val in d:
            if d[val] in counters:
                return False
            counters.append(d[val])
        return True
        
