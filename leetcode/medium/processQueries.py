class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        for i in range(1, m+1):
            p.append(i)
            
        res = []            
        for query in queries:
            i = 0
            while p[i] != query:
                i += 1
            res.append(i)
            p = [query] + p[0:i] + p[i+1:len(p)]
        
        return res
                
                
                
                
                
                
                
                
                
            
            
