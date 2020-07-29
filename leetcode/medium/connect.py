"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [root]
        while len(stack) > 0:
            temp = []
            for i in range(len(stack)):
                stack[i].next = (stack[i+1] if i+1 < len(stack) else None)
                if stack[i].left:
                    temp.append(stack[i].left)
                if stack[i].right:
                    temp.append(stack[i].right)
            stack = temp
        return root
                    
                    
                    

