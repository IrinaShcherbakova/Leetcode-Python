# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        right = self.postOrder(root.right, 0)
        root.val += right
        self.postOrder(root.left, root.val)
        return root
    
    
    def postOrder(self, root: TreeNode, sumNodes: int) -> int:
        if root is None:
            return sumNodes
        sumRight = self.postOrder(root.right, sumNodes)
        root.val += sumRight
        return self.postOrder(root.left, root.val)
        
