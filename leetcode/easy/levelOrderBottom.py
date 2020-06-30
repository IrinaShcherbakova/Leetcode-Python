# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curLength = len(stack)
            level = []
            # print("length %s " % curLength)
            for i in range(curLength):
                cur = stack.pop(0)
                if cur:
                    # print(cur.val)
                    level.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)
            if len(level) > 0:
                res.append(level)
        ans = []
        while len(res) > 0:
            ans.append(res.pop())
        return ans
                
