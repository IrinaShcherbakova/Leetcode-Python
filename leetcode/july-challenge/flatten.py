"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        first = head
        while head is not None:
            if head.child:
                head.child.prev = head
                tail = self.flattenChild(head.child)
                tail.next = head.next
                if head.next:
                    head.next.prev = tail
                head.next = head.child
                head.child = None
            head = head.next
        return first
    
     
    #returns a tail of the child's flattened list
    def flattenChild(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        prev = head
        while head is not None:
            if head.child:
                head.child.prev = head
                tail = self.flattenChild(head.child)          
                tail.next = head.next
                if head.next:
                    head.next.prev = tail
                head.next = head.child
                head.child = None
            prev = head
            head = head.next
        return prev
                
                
                
                
                
                
                
                
                
        
