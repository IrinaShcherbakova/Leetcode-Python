# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.traverse_path(root, sum, 0, [], res)
        return res
    
    
    def traverse_path(self, root: TreeNode, sum: int, current_sum: int, nodes: List[int], res: List[List[int]]) -> None:
        if not root:
            return 
        current_sum += root.val
        nodes.append(root.val)
        
        if current_sum == sum and not root.left and not root.right: 
            res.append(nodes)
            return
        
        self.traverse_path(root.left, sum, current_sum, nodes.copy(), res)
        self.traverse_path(root.right, sum, current_sum, nodes.copy(), res)
        return
