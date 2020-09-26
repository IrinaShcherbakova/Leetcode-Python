class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        poison_duration = 0
        x1, y1 = timeSeries[0], timeSeries[0] + duration
        for i in range(1, len(timeSeries)):
            x2, y2 = timeSeries[i], timeSeries[i] + duration
            if self.is_overlap(x1, y1, x2, y2):
                y1 = y2
            else:
                poison_duration += (y1 - x1)
                x1, y1 = x2, y2
        poison_duration += (y1 - x1)
        return poison_duration
    
    
    def is_overlap(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        return x2 >= x1 and x2 <= y1
