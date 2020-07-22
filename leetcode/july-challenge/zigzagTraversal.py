# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        isEven = True
        stack = [root]
        res = []
        while len(stack) > 0:
            length = len(stack)
            temp, level = [], []
            for i in range(length):
                cur = stack[i]
                level.append(cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            res.append(level[::-1] if not isEven else level)
            isEven = not isEven
            stack = temp
        return res
        
