"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodes = {}
        prev, first = None, None
        while head:
            if head not in nodes:
                node = Node(head.val, None, None)
                nodes[head] = node
            node = nodes[head]
            random = head.random
            if random and random not in nodes:
                nodes[random] = Node(random.val, None, None)
            if random:
                node.random = nodes[random]                      
            if not first:
                first = prev = node
            else:
                prev.next = node
                prev = prev.next
            head = head.next
        return first
                
            
