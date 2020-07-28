"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        return self.buildGraph(node, seen)
          
        
    def buildGraph(self, node: 'Node', seen: dict) -> 'Node':
        if not node:
            return None
        root = Node(node.val)
        seen[root.val] = root
        for neighbor in node.neighbors:
            if neighbor.val in seen:
                root.neighbors.append(seen[neighbor.val])
            else:
                newNeighbor = self.buildGraph(neighbor, seen)
                root.neighbors.append(newNeighbor)
        return root
                
                
                
                
                
