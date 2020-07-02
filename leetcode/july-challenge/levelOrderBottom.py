# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            curLen = len(stack)
            tempStack = []
            level = []
            for i in range(curLen):
                cur = stack[i]
                level.append(cur.val)
                if cur.left:
                    tempStack.append(cur.left)
                if cur.right:
                    tempStack.append(cur.right)
            res.append(level)
            stack = tempStack
        return res[::-1]
                
