# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt, nodes_sum = self.traverse(root)
        return tilt
    
    
    def traverse(self, root: TreeNode) -> tuple: #tilt so far, sum of subtree
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return 0, root.val
        left, right, tilt = 0, 0, 0
        if root.left:
            left_tilt, left = self.traverse(root.left)
            tilt += left_tilt
        if root.right:
            right_tilt, right = self.traverse(root.right)
            tilt += right_tilt
        tilt += abs(left-right)
        return tilt, root.val + left + right
