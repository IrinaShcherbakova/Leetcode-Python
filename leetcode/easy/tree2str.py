# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        res = str(t.val)
        if t.left is None and t.right is None:
            return res
        if t.left is None:
            res = res + "()"
        else:
            res = res + "(" + self.tree2str(t.left) + ")"
        if t.right is None:
            return res
        return res + "(" + self.tree2str(t.right) + ")"
        
        
        
        
        
        
