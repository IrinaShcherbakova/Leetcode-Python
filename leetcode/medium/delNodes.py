# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        delete = set()
        for num in to_delete:
            delete.add(num)
        res = []
        self.helper(root, delete, None, res)
        return res
        
        
        
    def helper(self, root: TreeNode, delete: set(), parent: TreeNode, res: List[TreeNode]) -> TreeNode:
        if root is None:
            return None
        if parent is None and root.val not in delete:
            res.append(root)
        
        #base case - leaf node
        if root.left is None and root.right is None:
            if root.val in delete:
                return None
            return root

        if root.val in delete:
            self.helper(root.left, delete, None, res)  
            self.helper(root.right, delete, None, res)  
            return None
        root.left = self.helper(root.left, delete, root, res)         
        root.right = self.helper(root.right, delete, root, res)  
        return root
        
            
            
            
            
            
            
            
            
            
            
            
