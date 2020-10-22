# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.traverse(root, 0)
        
    
    def traverse(self, root: TreeNode, count: int) -> int:
        if not root:
            return count
        
        count += 1
        if not root.left and not root.right:
            return count
        
        if not root.left or not root.right:
            return self.traverse(root.right, count) if not root.left else self.traverse(root.left, count)
        
        left = self.traverse(root.left, count)
        right = self.traverse(root.right, count)
        return min(left, right)
