"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        res = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            current = stack.pop()
            res.append(current.val)
            for i in range(len(current.children)-1,-1,-1):
                stack.append(current.children[i])
        return res
