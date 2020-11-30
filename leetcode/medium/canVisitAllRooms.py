class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = []
        for i in range(N):
            visited.append(False)
        has_key = set(rooms[0])   
        visited[0] = True
        
        while has_key:
            key = has_key.pop()
            if visited[key]:
                continue
            visited[key] = True
            has_key.update(rooms[key])
            
        for room in visited:
            if not room:
                return False
        return True
        
        
            
            
