# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        heap = []
        self.traverse(root1, heap)
        self.traverse(root2, heap)
        return [heappop(heap) for i in range(len(heap))]
    
    
    def traverse(self, root: TreeNode, nodes: List[int]) -> None:
        if not root:
            return
        heappush(nodes, root.val)
        self.traverse(root.left, nodes)
        self.traverse(root.right, nodes)
