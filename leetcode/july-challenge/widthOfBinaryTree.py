# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        maxWidth = 0
        first, last = -1, -1
        stack = [(root, 0)]
        while len(stack) > 0:
            temp = []
            for i in range(len(stack)):
                cur, index = stack[i][0], stack[i][1]
                if first < 0:
                    first = index
                if index > last:
                    last = index
                if cur.left:
                    temp.append((cur.left, 2*index))
                if cur.right:
                    temp.append((cur.right, 2*index+1))      
            if first == -1:
                return maxWidth
            maxWidth = max(maxWidth, last - first + 1)
            stack = temp
            first, last = -1, -1
        return maxWidth
                
            
            
