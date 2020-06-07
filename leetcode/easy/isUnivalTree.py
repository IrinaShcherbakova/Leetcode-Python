# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        rootValue = root.val
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            if current.val != rootValue:
                return False
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return True
        
