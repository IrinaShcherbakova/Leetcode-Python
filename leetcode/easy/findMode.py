# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        nodes = {}
        modeVal = 0
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.val in nodes:
                nodes[cur.val] = nodes[cur.val] + 1
            else:
                nodes[cur.val] = 1
            if nodes[cur.val] > modeVal:
                modeVal = nodes[cur.val]
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        ans = []
        for val in nodes:
            if nodes[val] == modeVal:
                ans.append(val)
        return ans
