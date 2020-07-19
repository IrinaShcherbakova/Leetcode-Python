# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        return self.insert(root, 1, True, v, d)
    
    
    def insert(self, root: TreeNode, depth: int, leftSide: bool, v: int, d: int) -> TreeNode:
        if depth == d:
            node = TreeNode(v)
            if leftSide:
                node.left = root
            else:
                node.right = root
            return node
        if root is None:
            return root
        root.left = self.insert(root.left, depth+1, True, v, d)
        root.right = self.insert(root.right, depth+1, False, v, d)
        return root
            
        
