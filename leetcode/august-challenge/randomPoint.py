class Rectangle:
    
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x_range = [x1, x2]
        self.y_range = [y1, y2]
        self.points = (x2 - x1 + 1) * (y2 - y1 + 1)
        self.min_points = 0
        self.max_points = 0
        

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rectangles = []
        self.total_points = 0
        for coord in rects:
            x1, y1, x2, y2 = coord[0], coord[1], coord[2], coord[3]
            rect = Rectangle(x1, y1, x2, y2)
            rect.min_points = self.total_points + 1
            self.total_points += rect.points
            rect.max_points = self.total_points
            self.rectangles.append(rect)
        

    def pick(self) -> List[int]:
        # pick a random point from the pool of all points
        point = random.randint(1, self.total_points)
        
        # locate the necessary rectangle
        rectangle = None
        for rect in self.rectangles:
            if point >= rect.min_points and point <= rect.max_points:
                rectangle = rect
                break
        
        # pick coordinates within this rectangle
        x_start, x_end = rectangle.x_range[0], rectangle.x_range[1]
        x = random.randint(x_start, x_end)
        y_start, y_end = rectangle.y_range[0], rectangle.y_range[1]
        y = random.randint(y_start, y_end)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
