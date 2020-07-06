# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.construct(preorder, 0, len(preorder))
    
    
    def construct(self, preorder: List[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        root = TreeNode(preorder[left])
        r = left + 1  #index of right element
        while r < right and preorder[r] < root.val:
            r += 1
        root.left = self.construct(preorder, left+1, r)
        root.right = self.construct(preorder, r, right)
        return root
