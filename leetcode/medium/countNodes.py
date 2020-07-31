# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        height, nodes = 0, 0
        stack = [root]
        while len(stack) > 0:
            nodes += len(stack)
            if len(stack) < 2 ** height:
                return nodes
            temp = []
            for node in stack:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            stack = temp
            height += 1
        return nodes
