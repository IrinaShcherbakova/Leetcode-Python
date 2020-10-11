# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nodes = []
        self.traverse_tree(root, nodes)
        nodes.sort()
        min_diff = nodes[1] - nodes[0]
        for i in range(1, len(nodes) - 1):
            cur_diff = nodes[i+1] - nodes[i]
            min_diff = min(min_diff, cur_diff)
        return min_diff
    
        
    def traverse_tree(self, root: TreeNode, nodes: List[int]) -> None:
        if not root:
            return
        nodes.append(root.val)
        self.traverse_tree(root.left, nodes)
        self.traverse_tree(root.right, nodes)
        return
