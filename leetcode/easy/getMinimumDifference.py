# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        values = self.inorder(root)
        minDist = abs(values[0] - values[1])
        for i in range(2, len(values)):
            minDist = min(minDist, abs(values[i]-values[i-1]))
        return minDist
            
            
    def inorder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        res = res + self.inorder(root.left)
        res.append(root.val)
        return res + self.inorder(root.right)
