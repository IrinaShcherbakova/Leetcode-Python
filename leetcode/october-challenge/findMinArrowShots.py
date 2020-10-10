class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_ballons = sorted(points, key=itemgetter(1,0))
        i = 0
        arrows = 0
        while i < len(sorted_ballons):
            j = i + 1
            while j < len(sorted_ballons) and self.overlaps(sorted_ballons[i], sorted_ballons[j]):
                j += 1
            arrows += 1
            i = j 
        return arrows
    
    
    def overlaps(self, interval1: List[int], interval2: List[int]) -> bool:
        x1, y1 = interval1[0], interval1[1]
        x2, y2 = interval2[0], interval2[1]
        return x2 <= y1
