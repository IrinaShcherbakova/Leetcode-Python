# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [[root, 0]]
        height = 0
        while len(stack) > 0:
            temp = []
            for i in range(2 ** height):
                if i == len(stack) and len(temp) > 0:
                        return False
                if i == len(stack) and len(temp) == 0:
                        return True
                node, index = stack[i][0], stack[i][1]
                if index != i:
                    return False
                if node.left:
                    temp.append([node.left, index*2])
                if node.right:
                    temp.append([node.right, index*2+1])
            stack = temp
            height += 1
        return True
