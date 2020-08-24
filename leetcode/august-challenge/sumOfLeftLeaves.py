# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return 0
        return self.dfs(root.left, True) + self.dfs(root.right, False)
    
    
    def dfs(self, root: TreeNode, is_left: bool) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return (root.val if is_left else 0)
        return self.dfs(root.left, True) + self.dfs(root.right, False)
