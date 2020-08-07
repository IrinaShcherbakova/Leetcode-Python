class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        total = 0
        row = 0
        while row < len(M):
            if M[row][row] == 2: #skip visited rows
                row += 1
                continue
            #create circle of friends of a person with id row
            circle = self.expand_circle(M, row)
            if circle:
                total += 1
            row += 1
        return total
    
    
    def expand_circle(self, M: List[List[int]], row: int) -> int:
        circle = 0
        stack = {row}
        while stack:
            cur_row = stack.pop()
            if M[cur_row][cur_row] == 2:
                continue
            for col in range(0, len(M[0])):
                if M[cur_row][col]:
                    circle += 1
                    stack.add(col)
            M[cur_row][cur_row] = 2
        return circle
            
                
            
            
            
            
            
            
            
            
            
            
