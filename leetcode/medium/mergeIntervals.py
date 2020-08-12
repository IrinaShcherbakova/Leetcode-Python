class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            temp = []
            while res and interval[1] < res[-1][0]:
                temp.append(res.pop())
            res.append(interval)
            self.validate_intervals(res)
            while temp:
                res.append(temp.pop())
        return res
    
    def validate_intervals(self, res: List[List[int]]) -> None:
        if len(res) < 2:
            return
        last, prev = res[-1], res[-2]
        
        if (last[0] >= prev[0] and last[0] <= prev[1]) or (last[1] >= prev[0] and last[1] <= prev[1]) or (last[0] <= prev[0] and last[1] >= prev[1]) or (last[1] <= prev[1]):
                x = min(last[0], prev[0])
                y = max(last[1], prev[1])
                res.pop()
                res.pop()
                res.append([x,y])
                self.validate_intervals(res)
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
   
