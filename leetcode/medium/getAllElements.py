# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        one = self.inorder(root1)
        two = self.inorder(root2)
        res = []
        i, j = 0, 0
        while i < len(one) and j < len(two):
            if one[i] < two[j]:
                res.append(one[i])
                i += 1
            elif one[i] >= two[j]:
                res.append(two[j])
                j += 1
        if i == len(one):
            return res + two[j:len(two)]
        return res + one[i:len(one)]
    
    
    def inorder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = self.inorder(root.left)
        res.append(root.val)
        return res + self.inorder(root.right)
