class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        self.findPath(graph, [], 0, target, res)
        return res
        
        
    def findPath(self, graph: List[List[int]], path: List[int], current: int, target: int, res: List[List[int]]) -> None:
        path.append(current)
        if current == target:
            res.append(path)
        else:    
            successors = graph[current]
            for successor in successors:
                newPath = list(path)
                self.findPath(graph, newPath, successor, target, res)
        
        
