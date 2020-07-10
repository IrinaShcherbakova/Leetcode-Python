# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res = res + self.inorderTraversal(root.right)
        return res
