# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxSum, maxLevel, level = root.val, 1, 1
        stack = [root]
        while len(stack) > 0:
            length = len(stack)
            temp = []
            levelSum = 0
            for i in range(len(stack)):
                levelSum += stack[i].val
                if stack[i].left:
                    temp.append(stack[i].left)
                if stack[i].right:
                    temp.append(stack[i].right)
            if levelSum > maxSum:
                maxSum, maxLevel = levelSum, level
            level += 1
            stack = temp
        return maxLevel
