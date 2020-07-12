# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            length = len(stack)
            temp = []
            maxVal = None
            for i in range(length):
                cur = stack[i]
                if maxVal is None or cur.val > maxVal:
                    maxVal = cur.val
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            stack = temp
            res.append(maxVal)
        return res
