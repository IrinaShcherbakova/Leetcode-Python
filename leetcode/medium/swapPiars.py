# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextPair = self.swapPairs(head.next.next)
        newHead = head.next
        newHead.next = head
        head.next = nextPair
        return newHead
        
        
