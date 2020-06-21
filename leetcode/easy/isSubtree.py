# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = [s]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.val == t.val and self.equalTrees(cur, t):
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
    
    def equalTrees(self, one: TreeNode, two: TreeNode) -> bool:
        stackOne = [one]
        stackTwo = [two]
        while len(stackOne) > 0 and len(stackTwo) > 0:
            curOne = stackOne.pop()
            curTwo = stackTwo.pop()
            if not curOne and not curTwo:
                continue
            if (not curOne and curTwo) or (curOne and not curTwo):
                return False
            if curOne.val != curTwo.val:
                return False
            stackOne.append(curOne.left)
            stackTwo.append(curTwo.left)
            stackOne.append(curOne.right)
            stackTwo.append(curTwo.right)
        return len(stackOne) == len(stackTwo) == 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
