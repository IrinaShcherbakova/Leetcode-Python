# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        return self.traverse(root, limit, 0)
    
    
    def traverse(self, root: TreeNode, limit: int, current: int) -> TreeNode:
        if not root:
            return root
        path_sum = current + root.val 
        if not root.left and not root.right:
            return (None if path_sum < limit else root)
        
        root.left = self.traverse(root.left, limit, path_sum)
        root.right = self.traverse(root.right, limit, path_sum)
        
        if root.left or root.right:
            return root
        
        return None
        
