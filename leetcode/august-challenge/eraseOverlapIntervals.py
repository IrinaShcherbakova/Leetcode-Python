class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(0,1))
        print(intervals)
        to_remove = 0
        index = 0
        for i in range(1, len(intervals)):
            x = intervals[index]
            y = intervals[i]
            if x[1] > y[0]:    # intervals are overlapping
                to_remove += 1
                index = (index if x[1] < y[1] else i)
            else:
                index = i
        return to_remove
