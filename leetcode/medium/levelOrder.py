"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        stack, res = [root], []
        while len(stack) > 0:
            length = len(stack)
            temp, level = [], []
            for i in range(length):
                cur = stack[i]
                level.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        if child:
                            temp.append(child)
            res.append(level)
            stack = temp
        return res
