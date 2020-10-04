class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=itemgetter(0))
        not_covered = []
        for interval in intervals:
            x1, y1 = interval[0], interval[1] #current interval
            if not not_covered:
                not_covered.append(interval)
                continue
            while not_covered:
                x2, y2 = not_covered[-1][0], not_covered[-1][1] #last cosidered interval
                if self.is_covered(x2, y2, x1, y1): #current interval covers last interval
                    not_covered.pop()
                elif self.is_covered(x1, y1, x2, y2): #last interval covers current interval
                    break
                else:  #intervals don't cover each other, append current
                    not_covered.append(interval)
                    break
        return len(not_covered)
                     
    
    # returns True if first interval is covered by the second
    def is_covered(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        return x2 <= x1 and y1 <= y2
