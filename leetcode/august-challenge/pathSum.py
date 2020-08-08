# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        sums, paths = self.traverse_path(root, sum)
        return paths
    
    
    # returns tuple - sum of the path below the current node and number of the found paths
    def traverse_path(self, root: TreeNode, target: int) -> tuple:
        if not root:
            return [], 0
        
        # print("visit %s" %root.val)
        paths = (1 if root.val == target else 0)
        # print("paths initial is %s" %paths)
        if not root.left and not root.right:
            return [root.val], paths
               
        left_sum, left_paths = self.traverse_path(root.left, target)
        right_sum, right_paths = self.traverse_path(root.right, target)
        # print("left sums: %s" %left_sum)
        # print("right sums: %s" %right_sum)
        
        all_sums = [root.val]
        
        while left_sum:
            cur = left_sum.pop()
            cur += root.val
            if cur == target:
                # print("path found at left at %s" %(cur-root.val))
                paths += 1
            all_sums.append(cur)
        
        while right_sum:
            cur = right_sum.pop()
            cur += root.val
            if cur == target:
                # print("path found at right at %s" %(cur-root.val))
                paths += 1
            all_sums.append(cur)
        
        paths = paths + left_paths + right_paths
        # print("all sums: %s" %all_sums)
        # print("all paths: %s" %paths)
        return all_sums, paths
        
        
        
        
        
        
        
        
        
        
        
        
        
