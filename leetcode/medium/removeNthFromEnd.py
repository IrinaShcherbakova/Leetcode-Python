# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head, position = self.traverse(head, n)
        return head
    
    
    def traverse(self, head: ListNode, n: int) -> tuple:
        
        if head.next is None: #we hit last node
            if n == 1:
                return None, 2
            else:
                return head, 2
        
        head.next, position = self.traverse(head.next, n)
        
        if position == n: #remove the current node
            return head.next, position + 1
        
        return head, position + 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
