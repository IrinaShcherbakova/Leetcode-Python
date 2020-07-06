# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        maxInd = 0
        for i in range(len(nums)):
            if nums[i] > nums[maxInd]:
                maxInd = i
        node = TreeNode(nums[maxInd])
        node.right = self.constructMaximumBinaryTree(nums[maxInd+1:len(nums)])
        node.left = self.constructMaximumBinaryTree(nums[0:maxInd])
        return node
