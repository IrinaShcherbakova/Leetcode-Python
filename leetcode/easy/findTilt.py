# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tiltSum = self.sumOfNodes(root)
        return tiltSum[1]
    
   
    #return 1) sum of nodes below 2) tiltSum of nodes below
    def sumOfNodes(self, root: TreeNode) -> List[int]:
        if root is None:
            return [0, 0]
        sumLeft = self.sumOfNodes(root.left)
        sumRight = self.sumOfNodes(root.right)
        tiltSum = abs(sumLeft[0] - sumRight[0])
        return [root.val + sumLeft[0] + sumRight[0], tiltSum + sumLeft[1] + sumRight[1]]
