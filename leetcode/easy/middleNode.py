# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast.next:
            if fast.next.next is None:
                return slow.next
            fast = fast.next.next
            slow = slow.next
        return slow
            
