# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sum_counts = {}
        self.traverse(root, sum_counts) 
        res = []
        for key in sorted(sum_counts, key=sum_counts.get, reverse=True):
            if not res or sum_counts[res[-1]] == sum_counts[key]:
                res.append(key)
            else:
                break
        return res
   

    def traverse(self, root: TreeNode, sum_counts: dict) -> int:
        if not root:
            return 0
        
        left_sum = self.traverse(root.left, sum_counts)
        right_sum = self.traverse(root.right, sum_counts)
        subtree_sum = root.val + left_sum + right_sum
        if subtree_sum in sum_counts:
            sum_counts[subtree_sum] += 1
        else:
            sum_counts[subtree_sum] = 1
        
        return subtree_sum
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
