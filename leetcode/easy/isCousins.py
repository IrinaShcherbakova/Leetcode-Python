# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        if root.val == x or root.val == y:
            return False
        xPar, xDepth = self.locateChild(root, x, 0)
        yPar, yDepth = self.locateChild(root, y, 0)
        if xPar is None or yPar is None:
            return False
        return (True if xDepth == yDepth and xPar.val != yPar.val else False)
        
            
    def locateChild(self, root: TreeNode, child: int, depth: int) -> tuple:
        if root is None:
            return None, None
        if root.left and root.left.val == child:
            return root, depth + 1
        if root.right and root.right.val == child:
            return root, depth + 1
        lPar, lDepth = self.locateChild(root.left, child, depth+1)
        rPar, rDepth = self.locateChild(root.right, child, depth+1)
        if lPar is not None:
            return lPar, lDepth
        return rPar, rDepth
        
        
        
        
        
        
        
