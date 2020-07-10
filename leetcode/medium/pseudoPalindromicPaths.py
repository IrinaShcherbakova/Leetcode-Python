# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.helper(root, [])
    
    
    def helper(self, root: TreeNode, path: List[int]) -> int:
        path.append(root.val)
        res = 0
        if root.left is None and root.right is None:            
            res = (1 if self.isPalindrome(path) else 0)
            path.pop()
            return res
        if root.left:
            res = self.helper(root.left, path)
        if root.right:
            res += self.helper(root.right, path)
        path.pop()
        return res
    
    
    #check if the given sequence of numbers could be transformed to
    # the palindrome
    def isPalindrome(self, nums: List[int]) -> bool:
        counts = [0] * 10
        for num in nums:
            counts[num] += 1
        oddFound = False
        for num in counts:
            if num % 2 != 0:
                if oddFound:
                    return False
                oddFound = True
        return True
