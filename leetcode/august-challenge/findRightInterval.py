class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return []
        start_index = {}
        max_start = intervals[0][0]
        for i, interval in enumerate(intervals):
            start, end = interval[0], interval[1]
            start_index[start] = i
            max_start = max(max_start, start)
                
        res = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            for i in range(end, max_start+1):
                if i in start_index:
                    res.append(start_index[i])
                    break
            else:
                res.append(-1)               
        return res
