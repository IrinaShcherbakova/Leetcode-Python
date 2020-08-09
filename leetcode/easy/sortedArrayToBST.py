# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.buildTree(nums, 0, len(nums))
        
    
    def buildTree(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        
        root_pos = left + ((right - left) // 2)
        # print("new root is %s" %nums[root_pos])
        root = TreeNode(nums[root_pos])
        root.left = self.buildTree(nums, left, root_pos)
        root.right = self.buildTree(nums, root_pos+1, right)
        return root
