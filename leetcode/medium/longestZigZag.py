# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        all_paths = set()
        if root.left:
            self.traverse(root.left, 1, True, all_paths)
        if root.right:
            self.traverse(root.right, 1, False, all_paths)
        return (max(all_paths) if all_paths else 0)
        
    
    def traverse(self, root: TreeNode, path: int, is_left: bool, all_paths: set) -> None:
        if not root.left and not root.right:
            all_paths.add(path)
            return
        
        if not root.left:
            all_paths.add(path)
            if is_left:
                return self.traverse(root.right, path+1, False, all_paths)
            else:
                return self.traverse(root.right, 1, False, all_paths)
                
        if not root.right:
            all_paths.add(path)
            if is_left:
                return self.traverse(root.left, 1, True, all_paths)
            else:
                return self.traverse(root.left, path+1, True, all_paths)
            
        if is_left:
            self.traverse(root.left, 1, True, all_paths)
            self.traverse(root.right, path+1, False, all_paths)
        else:
            self.traverse(root.left, path+1, True, all_paths)
            self.traverse(root.right, 1, False, all_paths)
        return
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
