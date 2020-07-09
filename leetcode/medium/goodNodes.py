# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodPaths(root, root.val)
    
    
    def goodPaths(self, root: TreeNode, parent: int) -> int:
        if root is None:
            return 0
        if root.val < parent:
            return self.goodPaths(root.left, parent) + self.goodPaths(root.right, parent)
        return 1 + self.goodPaths(root.left, root.val) + self.goodPaths(root.right, root.val)
