# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        numbers = []
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if self.existsSum(numbers, cur.val, k):
                return True
            else:
                numbers.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
    
    
    def existsSum(self, numbers: List[int], cur: int, k: int) -> bool:
        for num in numbers:
            if num + cur == k:
                return True
        return False
                
        
