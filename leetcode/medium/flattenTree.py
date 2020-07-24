# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.helper(root)
    
    #returns head and tail of the flattened subtree
    def helper(self, root: TreeNode) -> tuple:
        # print("visit %s" %root.val)
        if not root.left and not root.right:
            return root, root 
        if not root.left:
            rightHead, rightTail = self.helper(root.right)
            return root, rightTail
        if not root.right:
            root.right = root.left
            root.left = None
            rightHead, rightTail = self.helper(root.right)
            return root, rightTail            
        leftHead, leftTail = self.helper(root.left)
        # print("leftHead is %s, leftTail is %s" %(leftHead.val,leftTail.val))
        rightSubtree = root.right
        root.left = None
        root.right = leftHead
        rightHead, rightTail = self.helper(rightSubtree)
        # print("rightHead is %s, rightTail is %s" %(rightHead.val,rightTail.val))
        leftTail.right = rightHead
        # leftTail.left = None
        return root, rightTail
    
    
    
    
    
    
    
    
    
    
    
    
        
