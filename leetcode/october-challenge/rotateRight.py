# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 1
        
        #find length of the list
        first = head
        while first.next:
            length +=1
            first =first.next
        
        last = first
        k = length - k % length
        print("new k %s" %k)
        
        if k == length:
            return head
        #locate the last node of the rotated list
        #its position is equal to k
        current = 1
        first = head
        while current < k:
            current += 1
            first = first.next
        
        new_head = first.next
        first.next = None
        last.next = head
        head = new_head
        return head
