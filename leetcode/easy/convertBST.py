# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.postorder(root, 0)
        return root
        
               
    def postorder(self, root: TreeNode, totalSum: int) -> int:     
        if root.right:
            totalSum = self.postorder(root.right, totalSum)
        totalSum += root.val
        root.val = totalSum
        if root.left:
            totalSum = self.postorder(root.left, totalSum)    
        return totalSum
