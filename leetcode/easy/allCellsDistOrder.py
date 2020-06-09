class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        coord = [None] * (R*C)
        for i in range(R):
            for j in range(C):
                dist = abs(i-r0) + abs(j-c0)
                if coord[dist]:
                    coord[dist] = coord[dist] + [i,j]
                else:
                    coord[dist] = [i,j]
        ans = []
        for dist in coord:
            if dist:
                print(dist)
                i = 0
                while i < len(dist):
                    ans.append([dist[i],dist[i+1]])
                    i += 2
        return ans
                    
        
