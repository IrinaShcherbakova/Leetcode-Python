# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.inorder(root, nodes)
        return self.build_BST(nodes, 0, len(nodes))
        
    
    def inorder(self, root: TreeNode, nodes: List[int]) -> None:
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root.val)
        self.inorder(root.right, nodes)
        return
    
    
    def build_BST(self, nodes: List[int], left: int, right: int) -> TreeNode:
        if left == right:
            return None
        mid = left + (right-left) // 2
        root = TreeNode(nodes[mid])
        root.left = self.build_BST(nodes, left, mid)
        root.right = self.build_BST(nodes, mid+1, right)
        return root
