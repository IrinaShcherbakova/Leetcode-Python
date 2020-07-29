# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.path(root, 0)
    
    
    def path(self, root: TreeNode, numberSoFar: int) -> int:
        if root is None:
            return numberSoFar
        numberSoFar = numberSoFar * 10 + root.val
        if not root.left and not root.right:
            return numberSoFar
        if not root.left:
            return self.path(root.right, numberSoFar)
        if not root.right:
            return self.path(root.left, numberSoFar)
        # print("root is %s, number %s" %(root.val,numberSoFar))
        return self.path(root.left, numberSoFar) + self.path(root.right, numberSoFar)
