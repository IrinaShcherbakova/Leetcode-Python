# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        max_val, min_val, V = self.dfs(root)
        return max(V, abs(root.val - max_val), abs(root.val - min_val))
    
    
    def dfs(self, root: TreeNode) -> List[int]: # max subtree value, min subtree value, max V so far
        if not root.left and not root.right:
            return [root.val, root.val, 0]
        max_subtree_val, min_subtree_val, V = root.val, root.val, 0
        
        if root.left:
            left_max, left_min, left_V = self.dfs(root.left)
            max_subtree_val = max(left_max, max_subtree_val)
            min_subtree_val = min(left_min, min_subtree_val)
            V = max(left_V, abs(root.val - left_max), abs(root.val - left_min))
        
        if root.right:
            right_max, right_min, right_V = self.dfs(root.right)
            max_subtree_val = max(right_max, max_subtree_val)
            min_subtree_val = min(right_min, min_subtree_val)
            V = max(V, right_V, abs(root.val - right_max), abs(root.val - right_min))
                   
        return [max_subtree_val, min_subtree_val, V]
        
        
        
        
        
        
