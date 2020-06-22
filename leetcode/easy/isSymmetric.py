# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True 
        leftBranch = [root.left]
        rightBranch = [root.right]
        while len(leftBranch) > 0 and len(rightBranch) > 0:
            leftChild = leftBranch.pop()
            rightChild = rightBranch.pop()
            if not leftChild and not rightChild:
                continue
            if not leftChild:
                return False
            if not rightChild:
                return False
            if leftChild.val != rightChild.val:
                return False
            leftBranch.append(leftChild.left)
            leftBranch.append(leftChild.right)
            rightBranch.append(rightChild.right)
            rightBranch.append(rightChild.left)
        return True
            
            
            
            
            
            
            
