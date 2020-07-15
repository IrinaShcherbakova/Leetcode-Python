# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = self.helper(root, k, [])
        return node.val
    
    
    def helper(self, root: TreeNode, k: int, nodes: List[int]) -> TreeNode:
        if root.left:
            left = self.helper(root.left, k, nodes)
            if left:
                return left     
        nodes.append(root.val)
        if len(nodes) == k:
            return root
        if root.right:
            right = self.helper(root.right, k, nodes)
            if right:
                return right
        return None
        
        
