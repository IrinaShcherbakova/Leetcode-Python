# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def isBalanced(self, root: TreeNode) -> bool:
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur is None:
                continue
            left = self.getHeight(cur.left)
            right = self.getHeight(cur.right)
            if abs(left-right) > 1:
                return False
            stack.append(cur.left)
            stack.append(cur.right)
        return True
    
    
    def getHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return 1 + max(left, right)
