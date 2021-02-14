class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        
        for ball in range(lowLimit, highLimit+1):
            box = self.get_box_number(ball)
            if box in boxes:
                boxes[box] += 1
            else:
                boxes[box] = 1
        #print(boxes)
        return max(boxes.items(), key=operator.itemgetter(1))[1]
    
     
    def get_box_number(self, ball: int) -> int:
        sum_dig = 0
        while ball > 0:
            sum_dig += (ball % 10)
            ball //= 10
        return sum_dig
