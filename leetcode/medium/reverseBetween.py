# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        counter = 1
        cur, prev = head, None
        while counter < m:
            prev = cur
            cur = cur.next
            counter += 1
        last, localHead, tail = self.reverse(cur, counter, n)
        if prev:
            prev.next = localHead
        last.next = tail
        return (head if prev else localHead)
        
        
    #returns tail of new list, head of new list and next element after new list
    def reverse(self, head: ListNode, counter: int, n: int) -> List[ListNode]:
        if counter == n:
            return [head, head, head.next]
        last, newHead, tail = self.reverse(head.next, counter+1, n)
        last.next = head
        return [head, newHead, tail]
    
    
    
    
    
    
