# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seqOne = []
        stack = [root1]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.left is None and cur.right is None:
                seqOne.append(cur.val)
                continue
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        i = 0
        stack = [root2]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.left is None and cur.right is None:
                if i == len(seqOne) or seqOne[i] != cur.val:
                    return False
                i += 1
                continue
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return True
    
    

