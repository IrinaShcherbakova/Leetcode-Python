# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        root_rob, root_skip = self.traverse(root)
        return max(root_rob, root_skip)
          
    
    # tuple[0] - max amount of money if we rob this house 
    # tuple[1] - max amount of money if we skip this house
    def traverse(self, root: TreeNode) -> tuple:
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return root.val, 0
        left_rob, left_skip = self.traverse(root.left)
        right_rob, right_skip = self.traverse(root.right)
        cur_rob = left_skip + right_skip + root.val
        cur_skip = max(left_rob+right_rob, left_skip+right_skip, left_rob+right_skip, right_rob+left_skip)
        return cur_rob, cur_skip
    
    
    
                
        
        
        
        
