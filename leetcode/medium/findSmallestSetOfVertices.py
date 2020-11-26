class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        no_incoming = set()
        for i in range(n):
            no_incoming.add(i)
        
        has_incoming = set() 
        for edge in edges:
            fr, to = edge[0], edge[1]
            has_incoming.add(to)
        
        smallest_set = no_incoming.difference(has_incoming)
        return smallest_set
