# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        nodes = self.inOrder(root)
        newRoot = curr = TreeNode(nodes[0], None, None)
        for i in range(1, len(nodes)):
            curr.right = TreeNode(nodes[i], None, None)
            curr = curr.right
        return newRoot
         
        
    def inOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = [root.val]
        return self.inOrder(root.left) + res + self.inOrder(root.right)
             
