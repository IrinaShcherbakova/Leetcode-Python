# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even, evenHead = head.next, head.next
        while even:
            odd.next = even.next
            if not odd.next:
                even.next = None
                break
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return  head
        
            
        
