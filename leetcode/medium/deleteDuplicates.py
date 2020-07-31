# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, first = None, head
        while first:
            cur = first.next
            while cur and cur.val == first.val:
                cur = cur.next
            if first.next != cur:#we advanced current and have to delete first-cur
                if prev:
                    prev.next = cur
                else:
                    head = cur
            else:
                prev = first
            first = cur
        return head
                    
            
            
            
        
                
