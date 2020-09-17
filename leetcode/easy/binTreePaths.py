# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.traverse(root, "", res)
        return res
    
        
    def traverse(self, root: TreeNode, path: str, res: List[str]) -> None:
        if not root: 
            return
        if path:
            path = path + '->' + str(root.val)
        else:
            path += str(root.val)
        
        if not root.left and not root.right:
            res.append(path)
            return
        
        self.traverse(root.left, path, res)
        self.traverse(root.right, path, res)
        return
        
        
        
