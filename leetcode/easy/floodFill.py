class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        stack = [[sr,sc]]
        oldColor = image[sr][sc]
        while len(stack) > 0:
            cur = stack.pop()
            x = cur[0]
            y = cur[1]
            #check left neighbour
            if y - 1 >= 0 and image[x][y-1] == oldColor:
                stack.append([x,y-1])
            #check right neighbour
            if y + 1 < len(image[0]) and image[x][y+1] == oldColor:
                stack.append([x,y+1])
            #check top neighbour
            if x - 1 >= 0 and image[x-1][y] == oldColor:
                stack.append([x-1,y])
            #check bottom neighbour
            if x + 1 < len(image) and image[x+1][y] == oldColor:
                stack.append([x+1,y])
            image[x][y] = newColor
        return image
