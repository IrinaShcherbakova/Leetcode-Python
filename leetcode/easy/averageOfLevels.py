# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = [root.val]
        level = []
        if root.left:
            level.append(root.left)
        if root.right:
            level.append(root.right)
        while len(level) > 0:
            nextLevel = []
            avg = 0
            for node in level:
                avg += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(avg/len(level))
            level = nextLevel
        return res
        
