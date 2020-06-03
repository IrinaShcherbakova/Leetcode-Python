# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.buildTree(t1, t2, None)
        
    
    def buildTree(self, t1: TreeNode, t2: TreeNode, tree: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            tree = None
            return tree
        tree = TreeNode()
        if t1 is None:
            tree.val = t2.val
            tree.left = self.buildTree(t1, t2.left, tree.left)
            tree.right = self.buildTree(t1, t2.right, tree.right)
            return tree
        elif t2 is None:
            tree.val = t1.val
            tree.left = self.buildTree(t1.left, t2, tree.left)
            tree.right = self.buildTree(t1.right, t2, tree.right)
            return tree
        tree.val = t1.val + t2.val
        tree.left = self.buildTree(t1.left, t2.left, tree.left)
        tree.right = self.buildTree(t1.right, t2.right, tree.right)
        return tree
