"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        res = 1
        for child in root.children:
            childDepth = self.maxDepth(child) + 1
            if childDepth > res:
                res = childDepth
        return res
                
