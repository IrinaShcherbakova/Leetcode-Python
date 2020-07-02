# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return None
        # print(cloned.val)
        if target.val == cloned.val:
            return cloned
        left = self.getTargetCopy(original, cloned.left, target)
        if left is not None:
            return left
        return self.getTargetCopy(original, cloned.right, target)
        
      
