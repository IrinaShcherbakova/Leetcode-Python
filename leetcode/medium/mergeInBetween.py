# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        count = 0
        
        #locate a-1 node
        while count < a - 1:
            count += 1
            cur = cur.next 
        a_node = cur
        
        #locate b+1 node
        while count < b + 1:
            count += 1
            cur = cur.next
        b_node = cur
        
        a_node.next = list2
        cur = a_node
        while list2:
            cur = list2
            list2 = list2.next
        
        cur.next = b_node
        return list1
