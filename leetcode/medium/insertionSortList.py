# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        sorted_head = sorted_tail = head
        cur = head.next
        while cur:
            temp = cur.next
            sorted_head, sorted_tail = self.insert(sorted_head, sorted_tail, cur)
            cur = temp
        sorted_tail.next = None
        return sorted_head
    
    
    def insert(self, sorted_head: ListNode, sorted_tail: ListNode, cur: ListNode) -> tuple:
        if cur.val <= sorted_head.val:
            cur.next = sorted_head
            sorted_head = cur
            return sorted_head, sorted_tail
        
        if cur.val >= sorted_tail.val:
            sorted_tail.next = cur
            cur.next = None
            sorted_tail = cur
            return sorted_head, sorted_tail
        
        prev, insert_point = None, sorted_head
        while cur.val > insert_point.val:
            prev = insert_point
            insert_point = insert_point.next
            
        cur.next = insert_point
        prev.next = cur
        
        return sorted_head, sorted_tail
        
        
        
        
        
        
        
        
            
            
        
            
            
