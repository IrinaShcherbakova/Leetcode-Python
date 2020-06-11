class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = [0] * 5
        for char in text:
            if char == 'a':
                counts[0] += 1
            elif char == 'b':
                counts[1] += 1
            elif char == 'l':
                counts[2] += 1
            elif char == 'n':
                counts[3] += 1
            elif char == 'o':
                counts[4] += 1
        balloons = 0
        while True:
            if counts[0] >= 1:
                counts[0] -= 1
            else:
                return balloons
            if counts[1] >= 1:
                counts[1] -= 1
            else:
                return balloons
            if counts[2] >= 2:
                counts[2] -= 2
            else:
                return balloons
            if counts[3] >= 1:
                counts[3] -= 1
            else:
                return balloons
            if counts[4] >= 2:
                counts[4] -= 2
            else:
                return balloons
            balloons += 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            
