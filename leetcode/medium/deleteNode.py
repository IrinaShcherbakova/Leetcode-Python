# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        parent, original_root = None, root
        while root and root.val != key:
            parent = root
            if root.val > key:
                root = root.left
            elif root.val < key:
                root = root.right
        if not root:
            return original_root
        
        # delete leaf
        if not root.left and not root.right:
            if parent and parent.val > root.val:
                parent.left = None
                return original_root
            elif parent and parent.val < root.val: 
                parent.right = None
                return original_root
            return None
        
        # delete node with one child
        if not root.left or not root.right:
            if parent and parent.val > root.val:
                parent.left = (root.left if root.left else root.right)
                return original_root
            elif parent and parent.val < root.val: 
                parent.right = (root.left if root.left else root.right)
                return original_root
            return root.left if root.left else root.right
        
        # delete node with both children. Replace it with the leftmost node in the right subtree
        new_root, new_root_parent = root.right, root
        while new_root.left:
            new_root_parent = new_root
            new_root = new_root.left
        
        if new_root_parent != root:
            new_root_parent.left = new_root.right
        new_root.left = root.left
        new_root.right = (root.right if new_root_parent != root else new_root.right)
        
        if parent and parent.val < root.val:
            parent.right = new_root
        elif parent and parent.val > root.val:
            parent.left = new_root
        elif not parent:
            original_root = new_root
        return original_root
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
