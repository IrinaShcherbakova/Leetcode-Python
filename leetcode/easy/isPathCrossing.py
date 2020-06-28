class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {"00"}
        x, y = 0, 0
        for point in path:
            if point == 'N':
                y += 1
            elif point == 'E':
                x += 1
            elif point == 'S':
                y -= 1
            else:
                x -= 1
            cur = str(x) + str(y)
            if cur in visited:
                return True
            visited.add(cur)
        return False
