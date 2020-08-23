class DirectedEdge:
    
    def __init__(self, dest: int, weight: int):
        self.dest = dest
        self.weight = weight

# implements Dijkstra's algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # create vertex set of visited vertices
        visited = set()
        
        edgeFrom = {}
        for node in times:
            source, dest, time = node[0]-1, node[1]-1, node[2]
            edge = DirectedEdge(dest, time)
            if source in edgeFrom:
                edgeFrom[source].append(edge)
            else:
                edgeFrom[source] = [edge]
        
        distTo = [float('inf')] * N
        distTo[K-1] = 0
        
        # create set of working vertices
        V = []
        V.append([K-1, distTo[K-1]])
            
        while V:
            # sort vertices in V by distance
            V.sort(key=lambda x: x[1], reverse=True)
            
            # pop a vertex with a smallest distance
            vertex_data = V.pop()
            v, weight = vertex_data[0], vertex_data[1]
            visited.add(v)
            
            if v not in edgeFrom:
                continue
            
            # update distances of all adjacent neighbors
            for edge in edgeFrom[v]:
                u, dist = edge.dest, edge.weight
                if u in visited:
                    continue
                if distTo[u] > distTo[v] + dist:
                    distTo[u] = distTo[v] + dist
                    # update vertex distance in set V
                    for vertex_data in V:
                        if vertex_data[0] == u:
                            vertex_data[1] = distTo[u]
                            break
                    else:
                        V.append([u, distTo[u]])  #add vertex u to set V 
                        
        if len(visited) < N:
            return -1
        return max(distTo)
            
                    
            
            
            
           
    
    
    
    
    
    
    
    
    
   
