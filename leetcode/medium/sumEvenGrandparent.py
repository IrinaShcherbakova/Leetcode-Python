# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            curLen = len(stack)
            tempStack = []
            for i in range(curLen):
                cur = stack[i]
                if cur is None:
                    continue
                if cur.val % 2 == 0:  #found grandparent with even value
                    if cur.left:
                        if cur.left.left:
                            res += cur.left.left.val
                        if cur.left.right:
                            res += cur.left.right.val
                    if cur.right:
                        if cur.right.left:
                            res += cur.right.left.val
                        if cur.right.right:
                            res += cur.right.right.val
                tempStack.append(cur.left)
                tempStack.append(cur.right)
            stack = tempStack
        return res
                
                
                
                
                
                    
