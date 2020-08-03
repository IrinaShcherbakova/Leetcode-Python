# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildSubTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    
    def buildSubTree(self, preorder: List[int], pre_start: int, pre_end: int, inorder: List[int], in_start: int, in_end: int) -> TreeNode:
        # print("pre_start: %s" %pre_start)
        # print("pre_end: %s" %pre_end)
        # print("in_start: %s" %in_start)
        # print("in_end: %s" %in_end)
        if pre_start > pre_end or in_start > in_end:
            return None
        root = TreeNode(preorder[pre_start])
        # print("create node %s" %root.val)
        if pre_start == pre_end:
            return root
         
        # left subtree indeces
        in_left_end = in_start
        while in_left_end < len(inorder) and inorder[in_left_end] != root.val:
            in_left_end += 1
        pre_left_end = pre_start + (in_left_end - in_start)
        root.left = self.buildSubTree(preorder, pre_start+1, pre_left_end, inorder, in_start, in_left_end-1)
        
        # right subtree indeces
        root.right = self.buildSubTree(preorder, pre_left_end+1, pre_end, inorder, in_left_end+1, in_end)
        
        return root
        
            
        
        
        
        
        
        
        
        
        
