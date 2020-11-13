class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        index = 0
        length = len(intervals)
        
        while index < length and self.smaller(intervals[index], newInterval):
            res.append(intervals[index])
            index += 1
            
            
        while index < length and self.overlap(intervals[index], newInterval):
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1
            
        res.append(newInterval)
        
        for i in range(index, length):
            res.append(intervals[i])
            
        return res
             

    def overlap(self, i1: List[int], i2: List[int]) -> bool:
        x1, y1, x2, y2 = i1[0], i1[1], i2[0], i2[1]
        return (x2 >= x1 and x2 <= y1) or (x1 >= x2 and x1 <= y2)
    
    
    def smaller(self, i1: List[int], i2: List[int]) -> bool:
        y1, x2 = i1[1], i2[0]
        return x2 > y1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
