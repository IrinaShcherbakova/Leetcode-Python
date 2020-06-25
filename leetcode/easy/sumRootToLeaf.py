# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = self.findPaths(root)
        res = 0
        for path in paths:
            res += self.convertToDec(path)
        return res
        

    def findPaths(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        if not root.left and not root.right:
            return [[root.val]]
        leftBranch = self.findPaths(root.left)
        rightBranch = self.findPaths(root.right)
        res = []
        #print(root.val)
        if leftBranch:
            for path in leftBranch:
                path = [root.val] + path
                #print("left branch path %s " % path)
                res.append(path)
        if rightBranch:
            for path in rightBranch:
                path = [root.val] + path
                #print("right branch path %s " % path)
                res.append(path)   
        return res
    
    
    def convertToDec(self, path: List[int]) -> int:
        power = len(path) - 1
        res = 0
        #print(path)
        for num in path:
            #print(num)
            res = res + (num*(2**power))
            power -= 1
        #print(res)
        return res
        
        
        
    
