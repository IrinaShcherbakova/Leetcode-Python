# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        indeces_in = {}
        for i, node in enumerate(inorder):
            indeces_in[node] = i
        return self.buildSubTree(inorder, 0, len(inorder)-1, indeces_in, postorder, 0, len(postorder)-1)
    
    
    def buildSubTree(self, inorder: List[int], in_start: int, in_end: int, indeces_in: dict, postorder: List[int], post_start: int, post_end: int) -> TreeNode:
            if in_start > in_end:
                return None
            # print("root is %s" %postorder[post_end])
            if in_start == in_end:
                node = TreeNode(inorder[in_start])
                return node
            root = TreeNode(postorder[post_end])
            root_index_in = indeces_in[root.val]
            post_border = post_start + (root_index_in - in_start) #start from right subtree
            
            root.left = self.buildSubTree(inorder, in_start, root_index_in-1, indeces_in, postorder, post_start, post_border-1)
            root.right = self.buildSubTree(inorder, root_index_in+1, in_end, indeces_in, postorder, post_border, post_end-1)
            return root
            
