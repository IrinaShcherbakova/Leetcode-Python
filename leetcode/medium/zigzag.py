class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        for i in range(numRows):
            res.append("")
        
        cur = 0
        isDown = True
        
        for char in s:
            # print("cur is %s, char is %s, isDown %s" %(cur,char,isDown))
            res[cur] += char
            if isDown:
                cur = min(cur+1, numRows-1)
                if cur == numRows-1:
                    isDown = False
            else:
                cur = max(0, cur-1)
                if cur == 0:
                    isDown = True
                
        zigzag = ""
        for s in res:
            # print("s is %s" %s)
            zigzag += s
        return zigzag
                
            
            
            
