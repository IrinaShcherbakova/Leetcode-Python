# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        first, last = head, head
        cur = head.next
        last.next = None
        while cur:
            next_node = cur.next
            first, last = self.insert(first, last, cur)
            cur = next_node
        # print("result")
        # cur = first
        # while cur:
        #     print(cur.val)
        #     cur = cur.next
        return first
            
    
    def insert(self, head: ListNode, tail: ListNode, node: ListNode) -> tuple:
        prev, cur = None, head
        while cur and cur.val < node.val:
            prev = cur
            cur = cur.next
        if not cur: #insert at tail
            prev.next = node
            tail = node
            tail.next = None
        elif not prev: #insert at head
            node.next = head
            head = node
        else:
            node.next = cur
            prev.next = node
        return (head, tail)
        
