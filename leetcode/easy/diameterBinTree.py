# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_branch, max_path = self.traverse(root)
        return max_path
    
    def traverse(self, root: TreeNode) -> tuple:
        if not root.left and not root.right:
            return 0, 0
        left = right = left_path = right_path = 0
        if root.left:
            left, left_path = self.traverse(root.left)
            left += 1
        if root.right:
            right, right_path = self.traverse(root.right)
            right += 1
        cur_path = left + right
        max_path = max(left_path, right_path, cur_path)
        return max(left,right), max_path
            
