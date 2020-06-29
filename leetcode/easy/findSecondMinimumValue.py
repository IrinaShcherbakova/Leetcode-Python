# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        minVal, secondMin = root.val, None
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.val > minVal and (secondMin is None or cur.val < secondMin):
                secondMin = cur.val
            if not cur.left and not cur.right:
                continue
            if not cur.left:
                stack.append(cur.right)
                continue
            if not cur.right:
                stack.append(cur.left)
                continue
            stack.append(cur.left)
            stack.append(cur.right)
        return (-1 if secondMin is None else secondMin)
            
        
