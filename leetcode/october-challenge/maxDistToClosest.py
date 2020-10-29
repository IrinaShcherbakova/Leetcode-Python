class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start, end = None, None
        block = False
        max_dist = 0
        
        for i in range(len(seats)):
            if seats[i] == 0:
                if not block:
                    start, end = i, i
                    block = True
                else:
                    end = i
            elif seats[i] == 1 and i - 1 >= 0 and end == i - 1:
                cur_dist = self.find_max_dist(seats, start, end)
                max_dist = max(max_dist, cur_dist)
                block = False
        
        if start:
            cur_dist = self.find_max_dist(seats, start, end)
            max_dist = max(max_dist, cur_dist)
        return max_dist
    
    
    
    def find_max_dist(self, seats: List[int], start: int, end: int) -> int:
        if start == end:
            return 1
        if start == 0 or end == len(seats) - 1:
            return end - start + 1
        mid = start + (end - start) // 2
        return min(mid - start + 1, end - mid + 1)
        
                
