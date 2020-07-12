# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = root.val
        stack = [root]
        while len(stack) > 0:
            length = len(stack)
            res = stack[0].val
            temp = []
            for i in range(length):
                cur = stack[i]
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            stack = temp
        return res
                    
        
        
