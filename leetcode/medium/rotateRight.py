# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length, tail = self.numberOfNodes(head, 0)
        k = length - (k % length)
        if k == 0:
            return head
        cur, i = head, 1
        while i < k:
            cur = cur.next
            i += 1
        tail.next = head
        head = cur.next
        cur.next = None
        return head
        
    
    #returns number of nodes in a list and its tail
    def numberOfNodes(self, head: ListNode, count: int) -> tuple:
        if not head.next:
            return count+1, head
        return self.numberOfNodes(head.next, count+1)
        
