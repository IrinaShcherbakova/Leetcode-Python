# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isInLimits(root.left, root.val, None) and self.isInLimits(root.right, None, root.val)    
    
    def isInLimits(self, root: TreeNode, maxVal: int, minVal: int) -> bool:
        if not root:
            return True
        if maxVal is not None and root.val >= maxVal:
            return False
        if minVal is not None and root.val <= minVal:
            return False
        return self.isInLimits(root.left, root.val, minVal) and self.isInLimits(root.right, maxVal, root.val)
        
        
        
        
        
        
        
        
