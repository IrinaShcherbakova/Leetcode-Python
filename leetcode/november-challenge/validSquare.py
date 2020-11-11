class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        coordinates = [p1, p2, p3, p4]
        coordinates = sorted(coordinates, key=itemgetter(1,0))
        p1, p2, p3, p4 = coordinates[0],coordinates[1], coordinates[2], coordinates[3]
        a1 = self.side(p1, p2) 
        a2 = self.side(p1, p3) 
        a3 = self.side(p2, p4) 
        a4 = self.side(p3, p4)
        d1 = self.side(p1, p4)
        d2 = self.side(p2, p3)
        # in square all sides (a1, a2, a3, a4) are equal and diagonals (d1, d2) are equal
        return (a1 == a2 == a3 == a4) and (d1 == d2)
         
    
    def side(self, p1: List[int], p2: List[int]) -> int:
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
