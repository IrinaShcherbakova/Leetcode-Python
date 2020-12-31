# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        # if not root or root.val < val:
        #     node = TreeNode(val)
        #     node.left = root
        #     return node
        # if not root.left or root.left.val > val:
        #     root.left = self.insertIntoMaxTree(root.left, val)
        #     return root
        # root.right = self.insertIntoMaxTree(root.right, val)
        # return root
        A = self.get_A(root)
        A.append(val)
        return self.construct(A, 0, len(A))
        
        
    def get_A(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []
        return self.get_A(root.left) + [root.val] + self.get_A(root.right)
    
    
    def construct(self, nodes: List[int], left: int, right: int) -> TreeNode:
        if left == right:
            return None
        max_index = left
        for i in range(left+1, right):
            if nodes[i] > nodes[max_index]:
                max_index = i
        root = TreeNode(nodes[max_index])
        root.left = self.construct(nodes, left, max_index)
        root.right = self.construct(nodes, max_index+1, right)
        return root
    
    
    
    
    
    
         
