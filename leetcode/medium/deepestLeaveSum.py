# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        left, leftDepth = self.deepestLeave(root.left, 1)
        right, rightDepth = self.deepestLeave(root.right, 1)
        if leftDepth == rightDepth:
            return left + right
        if leftDepth > rightDepth:
            return left
        return right
    
    
    def deepestLeave(self, root: TreeNode, depth: int) -> tuple:
        if root is None:
            return None, depth
        if root.left is None and root.right is None:
            return root.val, depth + 1
        left, leftDepth = self.deepestLeave(root.left, depth+1)
        right, rightDepth = self.deepestLeave(root.right, depth+1)
        if left is None:
            return right, rightDepth
        if right is None:
            return left, leftDepth
        if leftDepth == rightDepth:
            return left + right, leftDepth
        if leftDepth > rightDepth:
            return left, leftDepth
        return right, rightDepth
        
        
        
        
        
        
