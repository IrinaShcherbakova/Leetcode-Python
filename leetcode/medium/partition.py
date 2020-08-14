# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        equal_or_greater = []
        prev, cur = None, head
        while cur:
            if cur.val >= x:
                equal_or_greater.append(cur)
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        for node in equal_or_greater:
            if prev:
                prev.next = node
                prev = prev.next
            else:
                prev = head = node
        prev.next = None
        return head
            
